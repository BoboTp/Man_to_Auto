#!/usr/bin/python

import os
import time
import csv
import re
from statistics import mean

##Looping wget for 10 Times

for i in range(0,10):
	#print("Number of wgets done :"+str(i))
	result=os.system("wget 200.200.3.1/abab.html |& tail -n 4 |awk '/MB/ {print $3}' >> /file_path/test.csv")





##Striping the '('and '\n' and finally appending the 10 values to a list-match

match = []
f = open('/file_path/test.csv', 'r')
for line in f.readlines():
	match.append(re.sub('[(]', '', line))
match = map(lambda s: s.strip(), match)
#print match
match2 = [float(x) for x in match]





##Average of all the values in the list, Final Value

def Average(match2):
	return mean(match2)

avg = Average(match2)
print(avg)



os.system("rm  /file_path/test.csv -f")
os.system("rm  rm abab.html* -f")
