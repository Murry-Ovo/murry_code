## This code will run a SQL script against Big Query and export the results as a CSV to specified location

import pandas as pd
from datetime import datetime as dt

#######################
### INPUT VARIABLES ###
#######################

## Specify filename 
filename = 'NPSSurvey_'

## Dateime to add to the filname
datetime = dt.now().strftime("%Y%m%d%H%M%S")

## Location to export the CSV to
path = 'C:\\NPS Output\\{}.csv'.format(filename,datetime)

## sql query to run, paste between the multi row quotes
sql_code = """
SELECT * 
FROM `data-science-retail.nps_secure.current_nps_sample`
"""

###################
### DOING STUFF ###
###################

## This rund the code saved to variable sql_code. think about replacing project_id with a variable
df = pd.read_gbq(sql_code,
                 project_id = 'data-science-retail',
                 dialect = 'standard')

## This saves the results of the code to the specified path
df.to_csv(path,
          index = False)
