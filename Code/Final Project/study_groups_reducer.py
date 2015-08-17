#!/usr/bin/python

# MapReduce Goal: We want to associate question node ID with student IDs
# 
# Output: Question_node_id student_id_lists

import sys
import operator

oldNodeId = None
studentList = list()

for line in sys.stdin:
    	data_mapped = line.strip().split("\t")

    	if len(data_mapped) != 2:
     		# Something has gone wrong. Skip this line.
        	continue
	
    	thisNodeId, thisStudent = data_mapped

    	if oldNodeId and oldNodeId != thisNodeId:
		# turn oldTag to string
		studentString = ','.join(studentList)

		# put the student IDs in brakets
		print oldNodeId, "\t[" + studentString + "]"
		studentList = list()

	oldNodeId = thisNodeId
    	studentList.append(thisStudent)

# do this for last node ID
studentString = ','.join(studentList)
print oldNodeId, "\t[" + studentString + "]"

