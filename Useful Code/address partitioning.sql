WITH 
Split_Addresses AS
(
SELECT 
      Account_No
      ,Full_Address
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(1)] AS Part1
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(2)] AS Part2
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(3)] AS Part3
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(4)] AS Part4
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(5)] AS Part5
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(6)] AS Part6
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(7)] AS Part7
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(8)] AS Part8
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(9)] AS Part9
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(10)] AS Part10
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(11)] AS Part11
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(12)] AS Part12
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(13)] AS Part13
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(14)] AS Part14
      ,SPLIT(Full_Address, ' ')[SAFE_ORDINAL(15)] AS Part15

      
FROM `data-science-retail.regs_and_compliance_secure.murry_temp_switching_overcharge_cheque_addresses` 
)

,Split_Addresses_With_Part_Count as
(
SELECT 
      if(Part1 IS NOT NULL,1,0) +
      if(Part2 IS NOT NULL,1,0) +
      if(Part3 IS NOT NULL,1,0) +
      if(Part4 IS NOT NULL,1,0) +
      if(Part5 IS NOT NULL,1,0) +
      if(Part6 IS NOT NULL,1,0) +
      if(Part7 IS NOT NULL,1,0) +
      if(Part8 IS NOT NULL,1,0) +
      if(Part9 IS NOT NULL,1,0) +
      if(Part10 IS NOT NULL,1,0) +
      if(Part11 IS NOT NULL,1,0) +
      if(Part12 IS NOT NULL,1,0) +
      if(Part13 IS NOT NULL,1,0) +
      if(Part14 IS NOT NULL,1,0) +
      if(Part15 IS NOT NULL,1,0) AS Parts
      ,*  

FROM Split_Addresses
)

-- where address splits into 4 parts
SELECT 
      part1 AS Address_Line_1
      ,'' AS Address_Line_2
      ,part2 AS Town
      ,part3 || ' ' || part4 AS Postcode
FROM
      Split_Addresses_With_Part_Count    
WHERE 
      PARTS = 4

-- where address splits into 4 parts
-- SELECT 
--       part1 || ' ' || part2 AS Address_Line_1
--       ,'' AS Address_Line_2
--       ,part3 AS Town
--       ,part4 || ' ' || part5 AS Postcode
-- FROM
--       Split_Addresses_With_Part_Count    
-- WHERE 
--       PARTS = 5