"""Script to call the OpsGenie Logs API to retrieve JSON data"""
import json
import re
import requests

def api_call(start_date, starting_file):
    """Call OpsGenie API, parse data, output data to external folder"""
    while True:
        call_api = f"https://api.opsgenie.com/v2/logs/list/{str(start_date)}?limit=5"
        headers = {'Authorization':'GenieKey xxxxxxxxxxxxxxxxxxxx'}
        list_of_filenames_url = requests.get(call_api,headers=headers)
        json_filenames = list_of_filenames_url.json()
        base_url = 'https://api.opsgenie.com/v2/logs/download/'
        if json_filenames["marker"]:
            pass
        else:
            global final_date
            final_date = start_date
            new_date = open(starting_file,'w')
            new_date.write(final_date)
            new_date.close()
            break

        start_date = json_filenames["marker"]

        for data in json_filenames["data"]:
            file_name = data["filename"] 
            file_endpoint = f"{base_url}{str(file_name)}"
            call_file_endpoint = requests.get(file_endpoint,headers=headers)
            result_from_endpoint = requests.get(call_file_endpoint.text)
            #print(result_from_endpoint.text)#THIS IS IT
            output_path = '/insert/path/to/output/folder/'
            output_file_name = output_path+file_name
            x = open(output_file_name,"w")
            x.write(result_from_endpoint.text)
            x.close()


def check_date_format(date_format, current_start_date, file_path):
    """Check to make sure OpsGenie's date format has not changed"""
    try:
        re.search(date_format, current_start_date)
        api_call(start_date=current_start_date, starting_file=file_path)
    except:
        raise Exception("Date format has changed, check OpsGenie Logs API doc page for new format")

def main():
    """starting point, declare variables, call other functions"""
    myregex='.+\-.+\-.+\-.+\-.+\-.+'  # pylint: disable=anomalous-backslash-in-string
    starting_file = '/path/to/starting/point/file'
    dates_file = open(starting_file,'r')
    start_date = dates_file.read()
    check_date_format(date_format=myregex, current_start_date=start_date, file_path=starting_file)
    dates_file.close()
