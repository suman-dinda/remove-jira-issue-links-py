#######################################
######Anaconda Python Interpreter######
######Author: Suman Dinda##############
######Website: suman-dinda.github.io###
#######################################
import json
import requests
from requests.auth import HTTPBasicAuth
import numpy
import readcsv
import getpass
import logging

hostname = input("Enter Hostname/BaseURL: ")
username = input("Enter Username: ")
password = getpass.getpass(prompt='Password: ') 
totalcount = 0
count = 0
currentIssueKey = ''
filePath = input("Enter CSV file Path(For windows use separator 'double backslash \\'): " or "test.csv")

readcsv_obj = readcsv.read_csv()
issueKeys = readcsv_obj._getdatafromcsv(filePath)
del issueKeys[0]
for ik in range(len(issueKeys)):
    getissuedetailsUrl = "https://"+hostname+"/rest/api/2/issue/"+issueKeys[ik][0]
    currentIssueKey = issueKeys[ik][0]
    auth = HTTPBasicAuth(username, password)
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "GET",
        getissuedetailsUrl,
        headers=headers,
        auth=auth
    )

    data = json.loads(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    fieldArray=[]
    for fields in data['fields']['issuelinks']: 
        fieldArray.append(fields)

    issue_links = json.loads(json.dumps(fieldArray))
    count = 0
    for i in range(len(issue_links)):
        if 'outwardIssue' in issue_links[i] and issue_links[i]['type']['outward'] == "Implements":
            logging.basicConfig(filename='output.txt', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
            logging.debug("===================================================")
            logging.info("|"+issue_links[i]['id'])
            delete_issuelinkid_url = issue_links[i]['self']
            count = count + 1
            totalcount = totalcount + 1

            logging.info("deleting issue link api url: " + delete_issuelinkid_url)
            auth = HTTPBasicAuth(username, password)
            headers = {
                "Accept": "application/json"
            }
            response = requests.request(
                "DELETE",
                delete_issuelinkid_url,
                headers=headers,
                auth=auth
            )
            logging.info(str(count) + ": Deleted issue link with id: "+ issue_links[i]['id'] + " from issue-key: "+ str(currentIssueKey))
            print(str(count) + ": Deleted issue link with id: "+ issue_links[i]['id'] + " from issue-key: "+ str(currentIssueKey))
            logging.debug("===================================================")
print("Total Issue Count Deleted: "+ str(totalcount))