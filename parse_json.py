import json, os
from pprint import pprint
import pandas as pd
import numpy as np

dic={}
d={}
uuid_arr=[]
logdate_arr=[]
path_to_json = '/home/user/Workplace/ZestIOT'
#place your directory over there
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

for js in json_files:
    with open(os.path.join(path_to_json, js)) as f:
    	for line in f:
    		#print line
		x= line.find("UUID")
		y= line.find("LogDate")
		uuid_start = x+10
		log_date_start = y+13
		uuid=""
		log_date=""
		while line[uuid_start]!="\\":
		  uuid+=line[uuid_start]
		  uuid_start+=1
		print "UUID : "+ uuid
		uuid_arr.append(uuid)
		while line[log_date_start]!="\\":
	   		log_date+=line[log_date_start]
	   		log_date_start+=1
		print "Log_date : "+ log_date
		logdate_arr.append(log_date)
		a=json.loads(line)
		d={(uuid,log_date):a}
		dic=dict(dic.items()+d.items())       
		dicc=dic		

	values = np.array(uuid_arr)
	for j in values:
		index = np.where(values == j)[0]
		if len(index) >1:
		   larg=0
		   for k in index: #da,,,,ivide entha
		      if logdate_arr[k] >= lang:
		        larg=logdate_arr[k]
		      else:
		        del dicc[(uuid,log_date)]
		        logdate_arr.remove(logdate_arr[k])
		        uuid_arr.remove(uuid_arr[k])
		print dicc
	print "hello"

