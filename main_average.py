#!/usr/bin/python

import os
import time
import csv
import re
import numpy as np
import pandas as pd
from itertools import izip

# Reading the Percentage loss csv and finding the average of it
df = pd.read_csv("/file_path/FinalSplit.csv",sep=",", header=None)
df = df.replace(")","")
#print(df)
for c in df.columns:
	df[c] = df[c].str.replace(r'\)', '')
	df[c] = df[c].str.replace(r'%', '')
	df[c] = df[c].str.replace(r'(', '').astype("float")
	a = df[c].mean()
	roundoff = round(a,2)
	#print(roundoff)
	with open('/file_path/beforetranspose.csv', 'a') as f:
     		writer = csv.writer(f, delimiter = ',')
     		for row in range(1):
			writer.writerow([roundoff])

a = izip(*csv.reader(open("/file_path/beforetranspose.csv", "rb")))
csv.writer(open("/file_path/Latest_410_avg.csv", "a")).writerows(a)



##########################################################################

# Reading the Throughput csv and finding the average of it
df = pd.read_csv("/file_path/thrusplit.csv",sep=",", header=None)
df = df.replace(")","")
#print(df)
for c in df.columns:
        a = df[c].mean()
        roundoff = round(a,2)
        #print(roundoff)
        with open('/file_path/thruputbeforetranspose.csv', 'a') as f:
                writer = csv.writer(f, delimiter = ',')
                for row in range(1):
                        writer.writerow([roundoff])

a = izip(*csv.reader(open("/file_path/thruputbeforetranspose.csv", "rb")))
csv.writer(open("/file_path/Latest_410_avgthruput.csv", "a")).writerows(a)



os.system("rm /file_path/beforetranspose.csv /file_path/thruputbeforetranspose.csv /file_path/FinalSplit.csv /file_path/thrusplit.csv -f")


f1 = open('/file_path/Latest_410_avg.csv')
f2 = open('/file_path/Latest_410_avgthruput.csv')
superout = open('/file_path/avg410avgthruput.csv','w')
for x in f2:
	try:
		y = next(f1)
        	superout.write(x.strip() + "," + y)
	except StopIteration:
    		pass

f3 = open('/file_path/Latest_410_version.csv')
f4 = open('/file_path/avg410avgthruput.csv')
superout = open('/file_path/final410.csv','w')
for x in f4:
	try:
		y = next(f3)
    		superout.write(x.strip() + "," + y)
	except StopIteration:
   		pass