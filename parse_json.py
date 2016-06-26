import json, os
from pprint import pprint
import pandas as pd
import numpy as np

dic={}
d={}
uuid_arr=[]
logdate_arr=[]
path_to_json = '/home/agil/intern'                        #place your directory over there(setting path to the file).
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

for js in json_files:
    with open(os.path.join(path_to_json, js)) as f:
      for line in f:
        x= line.find("UUID")                              #Creating a list of all the available UUIDs.
        y= line.find("LogDate")                           #Creating a list of all the available LogDates.
        uuid_start = x+10                                 #Assigning the starting index value of a UUID to a variable .      
        log_date_start = y+13                             #Assigning the starting index value of a LogDateto a variable.
        uuid=""
        log_date=""
        while line[uuid_start]!="\\":
          uuid+=line[uuid_start]
          uuid_start+=1                                   #Retrieving the UUID.
        print "UUID : "+ uuid
        uuid_arr.append(uuid)                             #inserting the UUID to the UUID list.
        while line[log_date_start]!="\\":
          log_date+=line[log_date_start]
          log_date_start+=1                               #Retrieving the LogDate.
        print "Log_date : "+ log_date
        logdate_arr.append(log_date)                      #inserting the UUID to the LogDate list.
        a=json.loads(line)
        d={(uuid,log_date):a}                             #Creating a dictonary with the UUID and LogDate as key.
        dic=dict(dic.items()+d.items())                   #Inserting all the elements to the dictonay by dictonary merge operation.
        dicc=dic    


for j in uuid_arr:
  values = np.array(uuid_arr)
  index = list(np.where(values == j)[0])                  #Finding the indexes of all the duplicate elements in the UUID list.
  if len(index) >1:
    larg=0
    for k in index:                                       #Finding the latest UUID by finding the largest LogDate.
      if logdate_arr[k] >= larg:
        larg=logdate_arr[k]
        l=k
    index.remove(l)
    p=0
    for k in index:
        if (uuid_arr[k-p],logdate_arr[k-p]) in dicc:
          del dicc[(uuid_arr[k-p],logdate_arr[k-p])]      #Removing the duplicate values from the dictonary.
        logdate_arr.remove(logdate_arr[k-p])              #Removing the duplicate values from the UUID list.
        uuid_arr.remove(uuid_arr[k-p])                    #Removing the duplicate values from the LogDate list.
        p=p+1
  print dicc                                              #Printig the dictonary of all the latest values without duplicate entries with respect to UUID.
  print dic                                               #Printig the dictonary of all the values with duplication.