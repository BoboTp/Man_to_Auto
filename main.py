#!/usr/bin/python

import os
import time
import csv
import re



os.system('''/file_path/iperfscript.py |awk '/sender|receiver/ { print$11","$12","$13","$6","$7","$8 }'> /file_path/tptp.csv''')


f = open('/file_path/tptp.csv')
r= re.compile('.*%\)')

csv_f = csv.reader(f)

row1=[]
row0=[]
for row in csv_f:
        row1.append(row[1])
	row0.append(row[0])
columnonelist = list(filter(r.match, row1))
columnzerolist = list(filter(r.match, row0))


a = []
b = []
a = columnonelist [1:11:2]
b = columnzerolist [1:21:2]

merge_list = a + b
print merge_list

with open('/file_path/FinalSplit.csv', 'a') as myfile:
	wr = csv.writer(myfile)
	wr.writerow(merge_list)

####################################################################################33

f = open('/file_path/tptp.csv')

csv_f = csv.reader(f)

row1=[]
row0=[]
row2=[]
for row in csv_f:
        row1.append(row[4])
        row0.append(row[3])
	row2.append(row[5])


a = []
b = []
a = row1 [1:10:2]
b = row0 [21:75:12]
c = row0 [91:185:22]



merge_list = a + b + c
print merge_list

with open('/file_path/thrusplit.csv', 'a') as myfile:
	wr = csv.writer(myfile)
     	wr.writerow(merge_list)

f.close()
