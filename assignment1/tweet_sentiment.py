import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    afinnfile = sent_file #open("AFINN-111.txt")
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  
    #print scores.items()
    
    for line in tweet_file:
        sum = 0
        try:
            tweetText = json.loads(line)["text"].encode('utf-8') #parse every tweet text
            #print re.findall(r"[\w']+", tweetText)
            for word in re.findall(r"[\w']+", tweetText): #Regex each word out
                if scores.has_key(word.lower()):
                    sum += scores[word.lower()]
            print sum
        except:
            pass

    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
