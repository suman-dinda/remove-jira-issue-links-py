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


file="C:\\Drive-D\\test\\issue-key.json"
f = open(file)
data = json.load(f)
issueKeyid=""
fieldArray=[]
for fields in data['fields']['issuelinks']: 
    fieldArray.append(fields)

issue_links = json.loads(json.dumps(fieldArray))
for i in range(len(issue_links)):
    if 'outwardIssue' in issue_links[i] and issue_links[i]['type']['outward'] == "Implements":
        print(issue_links[i]['id'])
f.close()