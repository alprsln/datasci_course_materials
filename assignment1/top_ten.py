import sys
import json
import re
import operator

def main():
    tweet_file = open(sys.argv[1])
    
    hashtags = {} # {hashtag, #repeated}

    for line in tweet_file:
        try:
            tweetHashtagList = json.loads(line)["entities"]["hashtags"]
            for tagDict in tweetHashtagList:
                tag = tagDict["text"].encode('utf-8')
                if hashtags.has_key(tag):
                    hashtags[tag] += 1
                else:
                    hashtags[tag] = 1
        except:
            pass
    
    topten = sorted(hashtags.items(), key=operator.itemgetter(1), reverse= True)[:10]

    for tag in topten:
        print tag[0] + " " + str(tag[1])

if __name__ == '__main__':
    main()