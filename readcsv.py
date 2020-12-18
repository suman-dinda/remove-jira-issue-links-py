#######################################
######Anaconda Python Interpreter######
######Author: Suman Dinda##############
######Website: suman-dinda.github.io###
#######################################

import json
import csv

class read_csv:
    issueKey=[]
    def _getdatafromcsv(self,path):
        fileUrl = path
        with open(fileUrl, mode ='r') as file:   
            csvFile = csv.reader(file) 
            for lines in csvFile: 
                self.issueKey.append(lines)
        return self.issueKey
