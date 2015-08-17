#!/usr/bin/python

# MapReduce Goal: Find the hour during which each student has posted
# the most posts. If there are ties, print all of them on 
# separate lines 
# 
# Mapper Goal: Print student ID and the hour for each post
#
# Output: Student_ID Hour


import sys
import csv

# read data
reader=csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if len(data) == 19:
	author_id = data[3][0:] #second square braket removes the quotation marks 
	datetime = data[8]
	
	index = datetime.find(":") #find where the first : is, and two digits before that is the hour
	hour = datetime[index-2:index]
	
	if hour[0] == "0": 
		hour = hour[1:2]
	if hour != "" and hour.isdigit():  # make sure hour is a digit and non-empty
		print "{0}\t{1}".format(author_id,hour)
