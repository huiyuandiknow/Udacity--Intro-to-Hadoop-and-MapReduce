#!/usr/bin/python

# MapReduce Goal: We want to associate question node ID with student IDs
#
# Mapper Goal: print the student id involved with each question (one per line). 
#              If it is a question, we will use the parent id to associate it 
#              with the original question id. 
# 
# Output: Question_node_id student_id

import sys
import csv

# read data from the .csv file
reader = csv.reader(sys.stdin, delimiter = '\t')
# skip field names
reader.next() 

for data in reader:
   	if len(data) == 19:	
		node_id = data[0] 
		author_id = data[3]
		node_type = data[5]
		parent_id = data[6]
		if parent_id == "" or node_type == "question":
			print node_id, "\t", author_id
		elif node_type == "answer":
			print parent_id, "\t", author_id


