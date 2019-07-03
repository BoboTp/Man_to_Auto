#!/usr/bin/python


# This is a script to run iperf between two machines and fint the Percentage loss and Throughput for UDP and throughput for TCP

# The program loops for three different Streams and five different Bandwidths (15 values)
 
import os
import time
import csv


stream=[1,5,10]

for x in stream:
        bandwidth=[1,5,10,25,50]
        for y in bandwidth:
		print('value of Number Of Streams=********'+str(x)+'*******and the value of Bandwidth is**********'+str(y)+'*********')
		result=os.system('iperf3 -c 200.200.3.1 -u -P'+str(x)+' -b '+str(y)+'M')
		time.sleep(5)