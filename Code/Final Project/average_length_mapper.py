#!/usr/bin/python

# MapReduce Goal: We want to process the forum_node data and output 
# the length of the post and the average answer length for each post. 
#
# Mapper Goal: Output the length associated with each Question node ID, 
# and then specify whether it's a question or answer
#
# Output: Question_Node_id post_length question_or_answer(text)

import sys
import csv

# read data from the .csv file
reader = csv.reader(sys.stdin, delimiter = '\t')

for data in reader:
    if len(data) == 19:	
        node_id = data[0] 
        title = data[1]
        body = data[4]
        node_type = data[5]
        parent_id = data[6]
        what= data[17]
	
	if body.startswith('"') and body.endswith('"'):
		body = body[1:-1]
	
	if node_id.isdigit():
		if parent_id == "" or node_type == "question":
			print node_id, "\t", len(body), "\t", "question" 
		elif node_type == "answer":
			print parent_id, "\t", len(body), "\t", "answer" 


