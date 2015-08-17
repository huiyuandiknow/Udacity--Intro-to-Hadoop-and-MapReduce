#!/usr/bin/python

# MapReduce Goal: Get the top tags in questions
#
# Mapper Goal: Print the tag for each question 
# Output: tags

import sys
import csv

# read data from the .csv file
reader = csv.reader(sys.stdin, delimiter = '\t')

# skip field names
reader.next() 

for data in reader:
   	if len(data) == 19:	
		tag = data[2] 
		node_type = data[5]
		parent_id = data[6]

		# empty parent id means it's a question
		if parent_id == "" or node_type == "question":
			# print 1 tag per line
			for t in tag.split():
				print t


