import requests
import json
import re

myregex='.+\-.+\-.+\-.+\-.+\-.+'
#had to insert absolute path for write_path to get to work
write_path = 'write.txt'
dates_file = open(write_path,'r')
day = dates_file.read()

i = 1
start_date = day

while re.search(myregex,start_date):
    i +=1
    first_get_url = 'https://api.opsgenie.com/v2/logs/list/'
    limit = '?limit=5'
    initial_get_call = first_get_url + str(start_date) + limit
    headers = {'Authorization':'GenieKey xxxxxxxxxxxxxxxxxxxx'}
    list_of_filenames_url = requests.get(initial_get_call,headers=headers)
    json_filenames = list_of_filenames_url.json()
    base_url = 'https://api.opsgenie.com/v2/logs/download/'

    new_date = ""
    
    if json_filenames["marker"]:
        place_holder=1
        ##print("Marker is "+json_filenames["marker"])
    else:
        global final_date
        final_date = start_date
        new_date = open(write_path,'w')
        new_date.write(final_date)
        break
   
    start_date = json_filenames["marker"]

    for data in json_filenames["data"]:
        filename = data["filename"] 
        get_endpoint = base_url + str(filename)
        endpoint = requests.get(get_endpoint,headers=headers)
        result_from_endpoint = requests.get(endpoint.text)
        #print(result_from_endpoint.text)#THIS IS IT
        file_path = '/insert/path/to/output/folder/'
        output_file = file_path+filename
        x = open(output_file,"w")
        x.write(result_from_endpoint.text)
        x.close()
    
else:
    print("Error: Invalid Start Date. Check Script")
    

dates_file.close()
new_date.close()
