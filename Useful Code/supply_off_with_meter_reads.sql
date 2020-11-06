WITH
CTE_Midnight_Snapshot_Data AS
      (
      SELECT 
            SAFE_CAST(SAFE_CAST(snapshotData.device.servicePointNumber AS NUMERIC) AS STRING) AS Meter_Point_no
            ,UPPER(snapshotData.device.serialNumber) AS Meter_Serial_no
            ,CAST(snapshotData.device.snapshotTime AS DATE) AS Read_Date
            ,snapshotData.device.cumulativeRegisters.activeImport AS Total_Reading       

      FROM 
           `data-engineering-prod.raw_andromeda_secure.rac_msd_received` 
      )

-- CTE containing all instances of a 'supply off' alarm being reported
-- Lead function used to identify the next supply off alarm
-- Reading on day of supply off being pulled through
,CTE_Supply_Off_Alarms AS
      (
      SELECT
            CAST(CAST(SA.servicePointNo AS NUMERIC) AS STRING) AS Meter_Point_No 
            ,UPPER(SA.deviceNo) AS Meter_Serial_No
            ,CAST(SA.occurrenceTime AS DATE) AS Supply_Off_Date
            ,SA.occurrenceTime AS Supply_Off_Datetime
            ,MSD.Total_Reading AS Supply_Off_Meter_Reading
            ,LEAD(SA.occurrenceTime,1,NULL)OVER(PARTITION BY SA.servicePointNo, SA.deviceNo ORDER BY SA.occurrenceTime) AS Next_Supply_Off_Datetime


      FROM
            `data-engineering-prod.raw_andromeda_secure.flow_SFE_ALARMS_validated` AS SA
            LEFT JOIN CTE_Midnight_Snapshot_Data AS MSD ON CAST(CAST(SA.servicePointNo AS NUMERIC) AS STRING) = MSD.Meter_Point_No
                                                           AND UPPER(SA.deviceNo) = MSD.Meter_Serial_No
                                                           AND CAST(SA.occurrenceTime AS DATE) = MSD.Read_Date                                                         
            
      WHERE
            -- 77 = Supply Off
            alarmCode = 77         
      )

-- Same as above but with the meter reading from the next supply off occurence being pulled through
-- This will be used to see if there has been any usage between 2 supply off alarms if there is no supply on alarm in between
,CTE_Supply_Off_Alarms_With_Next_Read AS
      (
      SELECT
            SA.Meter_Point_No 
            ,SA.Meter_Serial_No
            ,SA.Supply_Off_Date
            ,SA.Supply_Off_Datetime
            ,SA.Supply_Off_Meter_Reading
            ,SA.Next_Supply_Off_Datetime
            ,MSD.Total_Reading AS Next_Supply_Off_Meter_Reading

      FROM
            CTE_Supply_Off_Alarms AS SA
            LEFT JOIN CTE_Midnight_Snapshot_Data AS MSD ON SA.Meter_Point_No = MSD.Meter_Point_No
                                                           AND SA.Meter_Serial_No = MSD.Meter_Serial_No
                                                           AND CAST(SA.Next_Supply_Off_Datetime AS DATE) = MSD.Read_Date                                                                  
      )      

-- CTE containing all instances of a 'supply on (restoration of power)' alarm being reported
,CTE_Supply_On_Alarms AS
      (
      SELECT
            CAST(occurrenceTime AS DATE) AS Supply_On_Date
            ,occurrenceTime AS Supply_On_Datetime
            ,MSD.Total_Reading AS Supply_On_Meter_Reading
            ,CAST(CAST(servicePointNo AS NUMERIC) AS STRING) AS Meter_Point_No 
            ,UPPER(deviceNo) AS Meter_Serial_No

      FROM
            `data-engineering-prod.raw_andromeda_secure.flow_SFE_ALARMS_validated` AS SA
            LEFT JOIN CTE_Midnight_Snapshot_Data AS MSD ON CAST(CAST(SA.servicePointNo AS NUMERIC) AS STRING) = MSD.Meter_Point_No
                                                           AND UPPER(SA.deviceNo) = MSD.Meter_Serial_No
                                                           AND CAST(SA.occurrenceTime AS DATE) = MSD.Read_Date
            
      WHERE
            -- 75 = Supply On
            alarmCode = 75         
      ) 
-- ,CTE_Supply_Off_History AS
-- (
-- SELECT 
--       CURRENT_DATE() AS Snapshot_Date
--       ,SupOff.Meter_Point_No 
--       ,SupOff.Meter_Serial_No
--       ,MIN(SupOff.Supply_Off_Date) AS Supply_Off_Date
--       ,MIN(SupOff.Supply_Off_Datetime) AS Supply_Off_Datetime
--       ,SupOn.Supply_On_Date
--       ,SupOn.Supply_On_Datetime
--       ,SUM(DATE_DIFF(IFNULL(IFNULL(SupOn.Supply_On_Date,CAST(Next_Supply_Off_Datetime AS DATE)), CURRENT_DATE()), SupOff.Supply_Off_Date, DAY)) AS Days_Off_Supply
           
-- FROM 
--       CTE_Supply_Off_Alarms          AS SupOff
--       LEFT JOIN CTE_Supply_On_Alarms AS SupOn ON SupOff.Meter_Point_No = SupOn.Meter_Point_No
--                                                  AND SupOff.Meter_Serial_No = SupOn.Meter_Serial_No
--                                                  AND SupOn.Supply_On_Datetime BETWEEN SupOff.Supply_Off_Datetime AND IFNULL(SupOff.Next_Supply_Off_Datetime, current_timestamp())
                                                 
-- WHERE SupOff.Meter_Point_No  = '1317243805'

-- GROUP BY
-- 1,2,3,6,7      

-- ORDER BY MIN(SupOff.Supply_Off_Date)
-- )



,CTE_Supply_Off_History AS
(
SELECT 
      CURRENT_DATE() AS Snapshot_Date
      ,SupOff.Meter_Point_No 
      ,SupOff.Meter_Serial_No
      ,SupOff.Supply_Off_Date
--       ,SupOff.Supply_Off_Datetime
      ,SupOff.Supply_Off_Meter_Reading
      
      ,SupOn.Supply_On_Date
--       ,SupOn.Supply_On_Datetime
      ,SupOn.Supply_On_Meter_Reading
      ,DATE_DIFF(SupOn.Supply_On_Date,SupOff.Supply_Off_Date, DAY) AS Days_Off_Supply
      ,CASE
        WHEN DATE_DIFF(SupOn.Supply_On_Date,SupOff.Supply_Off_Date, DAY) = 0 THEN 0 
        ELSE (SupOn.Supply_On_Meter_Reading - SupOff.Supply_Off_Meter_Reading) / DATE_DIFF(SupOn.Supply_On_Date,SupOff.Supply_Off_Date, DAY) 
        END AS Daily_Usage_In_Sup_Off_Period
      
      ,CAST(SupOff.Next_Supply_Off_Datetime AS DATE) AS Next_Supply_Off_Date 
--       ,SupOff.Next_Supply_Off_Datetime
      ,SupOff.Next_Supply_Off_Meter_Reading
      ,DATE_DIFF(CAST(SupOff.Next_Supply_Off_Datetime AS DATE), SupOff.Supply_Off_Date, DAY) AS Days_Between_Off_Supply_Alarms
      ,CASE 
        WHEN  DATE_DIFF(CAST(SupOff.Next_Supply_Off_Datetime AS DATE), SupOff.Supply_Off_Date, DAY) = 0 THEN 0
        ELSE (SupOff.Next_Supply_Off_Meter_Reading - SupOff.Supply_Off_Meter_Reading) / DATE_DIFF(CAST(SupOff.Next_Supply_Off_Datetime AS DATE), SupOff.Supply_Off_Date, DAY) 
        END AS Daily_Usage_Between_Sup_Off_Alarms

      ,DATE_DIFF(IFNULL(IFNULL(SupOn.Supply_On_Date,CAST(Next_Supply_Off_Datetime AS DATE)), CURRENT_DATE()), SupOff.Supply_Off_Date, DAY) AS Days_Off_Supply2
      ,SupOn.Supply_On_Date IS NULL AS No_Subsequent_Supply_On_Alarm
           
FROM 
      CTE_Supply_Off_Alarms_With_Next_Read AS SupOff
      LEFT JOIN CTE_Supply_On_Alarms       AS SupOn ON SupOff.Meter_Point_No = SupOn.Meter_Point_No
                                                       AND SupOff.Meter_Serial_No = SupOn.Meter_Serial_No
                                                       AND SupOn.Supply_On_Datetime BETWEEN SupOff.Supply_Off_Datetime AND IFNULL(SupOff.Next_Supply_Off_Datetime, current_timestamp())  

ORDER BY
SupOff.Supply_Off_Date
)

SELECT * 
FROM CTE_Supply_Off_History
WHERE meter_point_no = '1317243805' 
ORDER BY Supply_Off_Date









