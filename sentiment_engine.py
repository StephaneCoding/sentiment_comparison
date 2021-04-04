import sys
#Obtenir des identifiants pour l’API Twitter
import tweepy 
#analyze sentiments
from textblob import TextBlob
import statistics
#Prise en charge des annotations de type exemple :def greeting(name: str) -> str:
from typing import List 
# When building Machine Learning systems based on tweet data, a preprocessing is required. 
# This library makes it easy to clean, parse or tokenize the tweets.
import preprocessor as p

#authentication with twitter developer account 
#os to get environment variables; it is a dictionary


apiKey = "ENTER YOUR KEY"
apiSecretKey = 'ENTER YOUR SECRET KEY'

auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
api = tweepy.API(auth)




def getTweets(keyword: str) -> List[str]: #retourne une liste de string (à titre informatif)
    allTweets = [] 
    #using extended mode, the text attribute of Status objects returned by tweepy.API methods replaced by a full_text attribute, 
    # which contains the entire untruncated text of the Tweet.
    #items(10)#iterate through the first 1000 tweets of that keyword
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode = "extended", lang = language).items(numberOfTweets): 
        allTweets.append(tweet.full_text)
    return allTweets
  

def cleanTweets(allTweets : List[str]) -> List[str]:
    tweetsClean = []
    for tweet in allTweets:
        tweetsClean.append(p.clean(tweet))
    return tweetsClean

def getSentiment(allTweets: List[str]) -> List[float]:
    sentimentScores = []
    for tweet in allTweets:
        #stock txt
        blob = TextBlob(tweet)
        # Each word in the lexicon has scores for:
        # 1)     polarity: -1 <= negative < 0 < positive <=1
        # 2) subjectivity: objective vs. subjective (+0.0 => +1.0)
        # 3)    intensity: modifies next word?      (x0.5 => x2.0)
        sentimentScores.append(blob.sentiment.subjectivity)
    return sentimentScores

def generateAverageSentimentScore(keyword: str) -> int:
    tweets = getTweets(keyword)
    tweetsClean = cleanTweets(tweets)
    sentimentScores = getSentiment(tweetsClean)
    averageScore = statistics.mean(sentimentScores)
    return averageScore


if __name__ == "__main__":
    print(apiKey)
    print(apiSecretKey)   
    try:
        print('Enter the number of tweets you want to put on the polling')
        numberOfTweets = int(input())
    except ValueError:
        print("ERROR: You have to enter an integer. Try again \n")
    else:
        print("In which language do you want these tweets? fr or en?")
        language = input()
        if(language == "fr" or language == "en"):
            pass
        else:
            print("ERROR: You have to enter either fr or en. Try again\n")
            sys.exit()
        print("What does the world prefer?")
        firstThing = input()
        print("... or ...")
        secondThing = input()
        print("\n")
        firstScore = generateAverageSentimentScore(firstThing)
        secondScore = generateAverageSentimentScore(secondThing)
        if (firstScore > secondScore):
            print(f"People prefer {firstThing} over {secondThing}")
        elif(firstScore == secondScore):
            print(f"People prefer {secondThing} as much as {firstThing}")
        else:
            print(f"People prefer {secondThing} over {firstThing}")
