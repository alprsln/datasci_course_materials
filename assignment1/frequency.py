import sys
import json
import re

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    
    freqDict = {} #{word, wordRepeatAmount}
    
    #wordCount = 0
    for line in tweet_file:
        tweetText = json.loads(line)["data"]["text"].encode('utf-8') #parse every tweet text
        tweetWords = re.findall(r"[\w']+", tweetText) #Regex each word out
        for wordCaps in tweetWords: 
            word = wordCaps.lower()
            #wordCount += 1
            if not freqDict.has_key(word): #if word isn't in dict, add to dict
                freqDict[word] = 1.0
            else:
                freqDict[word] += 1 #else increase wordRepeat by 1
    #print len(freqDict)
    for word, repeatAmount in freqDict.items():
        wordFreq = repeatAmount/len(freqDict)
        print word + " " + str(wordFreq)

if __name__ == '__main__':
    main()
