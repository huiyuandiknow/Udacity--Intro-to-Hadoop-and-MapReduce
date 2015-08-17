#!/usr/bin/python

# MapReduce Goal: Find the hour during which each student has posted
# the most posts. If there are ties, print all of them on 
# separate lines 
# 
# Output: Student ID | Hour at which student posts the most

import sys
import operator
from collections import defaultdict

listofHour = defaultdict(int)
oldId = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
	
    thisId, thisHour = data_mapped

    if oldId and oldId != thisId:
	highestCount = max(listofHour.values())
	for k,v in listofHour.items():
		if v == highestCount:
			print oldId, "\t", k
        oldId = thisId;

	#reinitialize for another id
	listofHour = defaultdict(int) 

    oldId = thisId
    listofHour[thisHour] += 1

highestCount = max(listofHour.values())
for k,v in listofHour.items():
	if v == highestCount:
		print oldId, "\t", k
