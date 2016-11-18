#!/usr/bin/env python


import sys, math, nltk
sys.path.append('./')


def readFileandReturnAnArray(fileName, readMode, isLower):
    myArray=[]
    with open(fileName, readMode) as readHandle:
        for line in readHandle.readlines():
            lineRead = line
            if isLower:
                lineRead = lineRead.lower()
            myArray.append(lineRead.strip().lstrip())
    readHandle.close()
    return myArray


for line in sys.stdin:
    try:
        Tokens = nltk.word_tokenize(line)
        length = len(Tokens)
        topicfiles =["topic1","topic2","topic3"]
        for i in topicfiles:
            alphabet = readFileandReturnAnArray(i, "r", True)
            topicId = alphabet.pop(0)
            freqList = []
            for symbol in alphabet:
                words = nltk.word_tokenize(symbol)
                if words.__len__() ==2:
                        cnt1 = Tokens.count(words[0])
                        cnt2 = Tokens.count(words[1])
                        if (cnt1 == cnt2):
                                cnt = cnt1
                        elif (cnt1<cnt2):
                                cnt = cnt1
                        else:
                                cnt = cnt2
                else:
                        cnt = Tokens.count(symbol)
                if cnt != 0:
                    wordProb = float(cnt)/length
                    freqList.append(wordProb)
            # Shannon entropy
            ent = 0.0
            for freq in freqList:
                ent = ent + float(freq) * math.log(freq, 2)
            if ent != 0.0:
                ent = -ent
                print '%s\t%s' % (topicId,ent)
    except ValueError:
        continue
