#!/usr/bin/python

# MapReduce Goal: Get the top tags in questions
#
# Output: tags number_of_times_used

import sys
import operator

oldTag = None
count = 0
tagList = dict()

for line in sys.stdin:
    	data_mapped = line.strip().split("\t")

    	if len(data_mapped) != 1:
     		# Something has gone wrong. Skip this line.
        	continue
	
    	thisTag = data_mapped

    	if oldTag and oldTag != thisTag:
		# turn oldTag to string
		tagString = ''.join(oldTag)
		tagList[tagString] = count
        	oldTag = thisTag
		count = 0

	oldTag = thisTag
    	count += 1

# do this for last tag word
tagString = ''.join(oldTag)
tagList[tagString] = count

# sort tagList by value to get top 10 most tagged
sorted_tag = sorted(tagList.items(), key=operator.itemgetter(1), reverse=True) #sort descending order
for k, v in sorted_tag[0:10]: 
	print ''.join(k), "\t", v
