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
    
    unknownDict = {} #{word, [allCountedScores]}
    
    for line in tweet_file:
        _sum = 0
        try:
            tweetText = json.loads(line)["text"].encode('utf-8') #parse every tweet text
            tweetWords = re.findall(r"[\w']+", tweetText) #Regex each word out
            lineDict = {} #{word, score}
            for wordCaps in tweetWords: 
                word = wordCaps.lower()
                #if word isn't in AFINN, add to dict
                if not scores.has_key(word):
                    if not lineDict.has_key(word):
                        lineDict[word] = 0
                #if word is in AFINN, add to score
                if scores.has_key(word): 
                    _sum += scores[word]
            #add accumulated score to all nonAFINN words
            for word in lineDict: 
                #print(word)
                lineDict[word] = _sum
            #merge lineDict into unknownDict
            for word in lineDict:
                if not unknownDict.has_key(word):
                    unknownDict[word] = [lineDict[word]]
                else:
                    unknownDict[word].append(lineDict[word])
        except:
            pass

    #Calculate weighted scores of all words in unknownDict
    sentimentDict = {} # {word, weightedScore}
    for word, scores in unknownDict.items():
        _sum = sum(scores, 0.0)
        sentimentDict[word] = _sum / len(scores)

    for word, score in sentimentDict.items():
        print word + " " + str(score)

    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
