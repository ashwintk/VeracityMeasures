#!/usr/bin/env python

from operator import itemgetter
import sys

def readFileandReturnAnArray(fileName, readMode, isLower):

    with open(fileName, readMode) as readHandle:
        for line in readHandle.readlines():
            lineRead = line
            if isLower:
                lineRead = lineRead.lower()
            count = (lineRead.strip().lstrip())
    readHandle.close()
    return count

totalTweetCount = readFileandReturnAnArray("tweetCount", "r", True)
totalTweetCount = float(totalTweetCount)

geo_score = {}

for line in sys.stdin:
    line = line.strip()
     #topicId, location = line.split('\t')  #Could not partition using split so figured out another way
    if line!="" and line is not None:       #due to error line[0] is index out of range
        topicId = line[0]                   #line[0] has topicId
        if line[2:] is not None:            #from line[2] is the location
            location = line[2:]
        else:
            location = None

        if topicId in geo_score:
                existingValues = geo_score.get(topicId)
                if location is not "" and location != None and location not in existingValues and location!="noLocation":
                        geo_score[topicId].append(location)
        else:
                if topicId == "1" or  topicId == "2" or  topicId == "3":          #as the ouptut gives some special characters
                        geo_score[topicId] = []
                        if location is not "" and location != None and location!="noLocation":
                                geo_score[topicId].append(location)


for topic in geo_score.keys():
    list_of_values = geo_score[topic]
    length = len(list_of_values)
    final_score = float(length)/totalTweetCount
    print '%s\t%s'% (topic, final_score)
