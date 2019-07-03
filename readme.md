###Automating Manual Test Cases

This is a script to run iperf between two machines and fint the Percentage loss and Throughput for UDP and throughput for TCP


The program loops for three different Streams and five different Bandwidths (15 values)


The Output after running Iperf is stored to a separate csv files(one for throughput and one for Percentage Loss), multiple regex pattern is used to split them and put it in respective csv.

To run the tests on multiple machines we use ansbile playbooks and cronjobs for it to run it fully automated in regular intervals.

The iperfscript is looped multiple times and finally the average of it represents that particular days performance.

If we have multiple versions of a product through which we can pass the traffic, we can switch between the builds and see how it changes and the performance gain/loss.

Similarly the Wget and SCP commands are used to generate a report everyday, with which we can analyze the performance change.
