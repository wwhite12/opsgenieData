import requests
import json
import re

myregex='.+\-.+\-.+\-.+\-.+\-.+'
starting_file = '/path/to/starting/point/file'
dates_file = open(starting_file,'r')
start_date = dates_file.read()

while re.search(myregex,start_date):

    initial_call = f"https://api.opsgenie.com/v2/logs/list/{str(start_date)}?limit=5"
    headers = {'Authorization':'GenieKey xxxxxxxxxxxxxxxxxxxx'}
    list_of_filenames_url = requests.get(api_call,headers=headers)
    json_filenames = list_of_filenames_url.json()
    base_url = 'https://api.opsgenie.com/v2/logs/download/'
    
    if json_filenames["marker"]:
        pass
        ##print("Marker is "+json_filenames["marker"])
    else:
        global final_date
        final_date = start_date
        new_date = open(starting_file,'w')
        new_date.write(final_date)
        break
   
    start_date = json_filenames["marker"]

    for data in json_filenames["data"]:
        file_name = data["filename"] 
        file_endpoint = f"{base_url}{str(file_name)}"
        call_file_endpoint = requests.get(file_endpoint,headers=headers)
        result_from_endpoint = requests.get(endpoint.text)
        #print(result_from_endpoint.text)#THIS IS IT
        output_path = '/insert/path/to/output/folder/'
        output_file_name = output_path+file_name
        x = open(output_file_name,"w")
        x.write(result_from_endpoint.text)
        x.close()
    
else:
    print("Error: Invalid Start Date. Check Script")
    

dates_file.close()
new_date.close()
