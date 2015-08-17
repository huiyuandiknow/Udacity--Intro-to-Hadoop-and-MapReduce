#!/usr/bin/python

# MapReduce Goal: We want to process the forum_node data and output 
# the length of the post and the average answer length for each post. 
#
# Output: Question_Node_id Question_length Average_answer_length

import sys
import operator
from collections import defaultdict

# dict() could do the job as well, but since we do not need 
# to keep the values after each iteration, it's better to 
# use simple temporary variables 

oldId = None
answerCount = 0
totalAnswerLength = 0
questionLength = 0
questionCount =0

for line in sys.stdin:

    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue
	
    thisId, thisLength, thisType = data_mapped

    if oldId and oldId != thisId:
	if questionCount !=0:
		# If there's no answer, then the count is 0
		if answerCount == 0: 
			output = 0
		else:
			output = totalAnswerLength/answerCount
		print oldId, "\t", questionLength, "\t", output
        oldId = thisId;
	answerCount = 0
	totalAnswerLength = 0
	questionLength = 0
	questionCount = 0

    oldId = thisId
    #check what type it is 
    if thisType == "question": 
	questionLength = thisLength
	questionCount = 1
    elif thisType == "answer":
	totalAnswerLength += float(thisLength) #conversion needed for arithmetics 
	answerCount +=1

# repeat steps for last question node ID
if questionCount !=0:
	if answerCount == 0: 
		output = 0
	else:
		output = totalAnswerLength/answerCount
	print oldId, "\t", questionLength, "\t", output
