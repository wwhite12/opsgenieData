# opsgenieData

## Overview
Python Script that utilizes the OpsGenie Alert Mangement Logs API to continuously output all logs recoreded by the OpsGenie platform 

## Requirements 
- An OpsGenie Alert Management account with an API Key. 
- Requests Python Module

## Instructions
Copy or fork this repo to place this script on your local. Go to your OpsGenie UI and retrieve your API Key("GenieKey"). Place the API Key in the script in the variable "headers"(DO NOT remove GenieKey from the script, just replace the xxxxxx the API Key. This is needed to make calls to your Logs API. Install requests for GET calls to the Logs API. It is recommended that you create a folder also containing an output folder. Insert the path to this folder in the "file_path" variable on line 44 of the script. This is where the files of data will be placed. Next, create a file called "write.txt". This will be the starting date where the script will start pulling data from, and work towards the present. NOTE: the start date in write.txt must be in correct format(2020-05-15-12-00-00)and also note that OpsGenie dates are on UTC time. Be sure to put the path to the write.txt file in the "write_path" variable on line 7. After all this the script should be good to start pulling in data. 

## Pulling in Recent Data
If your start date in write.txt is a recent date(30 minutes ago-2 days ago), the script should take anywhere from 5-60 minutes to pull in all data(depending on amount of data there is for your team). Once the script is done and it can't pull in anymore data, the stopping point date will be stored as a marker in write.txt for the starting point of the next script run.

## Pulling in Large Amount of Data
If your start date in write.txt is from a much older date(a few weeks or months ago), the script will take a few days to pull in all data up to the present. Once it is done, it will also store the stopping marker date in write.txt to use as the starting point for the next script run. 

## Use-Cases
- The OpsGenie Alert Management System does have their Logs API visible on their UI, however these logs only go back 13 days. If certain alerts, policies, or integration changes/deletions were made earlier than 13 days ago, that data would be lost unless pulled in to scan through via this script
- Ingesting all OpsGenie logs in a log monitoring tool (i.e. Splunk) for more in depth analysis of alerting or creation of faster dashboards.

## Further Documentation
This script makes use of multiple API calls per loop as OpsGenie's Logs API retrieval procedure is very intricate. You can read the full documentation of OpsGenie's Logs API here: https://docs.opsgenie.com/docs/logs-api 

## Questions
If you have any questions regarding this script or need any help please feel free to reach out to me at willcwhite@gmail.com

### Creator
William White
