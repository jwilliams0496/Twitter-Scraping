from twython import Twython
import time

username = "JonTronShow"
hashtag = "jontronshow"
searchType = 1
searchSize = 100

def main():
    tweetData = readDataFile("dataFile.txt")

    print(tweetData)
    print(len(tweetData))
    
def vectorizeData(words):
    pass

def readDataFile(fileName):
    dataFile = open(fileName, 'r')
    return dataFile.read()
    
def getData():
    accessToken = getKeys()[0]
    accessTokenSecret = getKeys()[1]
    consumerKey = getKeys()[2]
    consumerSecret = getKeys()[3]

    print(accessToken)
    print(accessTokenSecret)
    print(consumerKey)
    print(consumerSecret)
    
    print("Obtaining OAuth 2 token\n\n")

    twitter = Twython(consumerKey, consumerSecret, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_accessToken()

    print("Access token granted\n")

    twitter = Twython(consumerKey, accessToken=ACCESS_TOKEN)

    if (searchType == 0):
        userTimeline = twitter.get_userTimeline(screen_name = username)
        
        print("\n\nTweets from ", username, "\n\n")
        
        # And print the tweets for that user.
        for tweet in userTimeline:
            print(tweet['text'])
            
        user_retweets = twitter.get_retweets(screen_name = username)
            
        print("\n\nRe-Tweets from ", username, "\n\n")

        for retweet in user_retweets:
            print(retweet['text'])
        
    if (searchType == 1):
        print("Searching for tweets\n")
        
        tweetIds = {}

        search = twitter.search(q=hashtag, count=searchSize)
        tweets = search['statuses']

        for tweet in tweets:
            print(tweet['id_str'], '\n', tweet['text'], '\n\n\n')
  
            if (tweet['id_str'] not in tweetIds):
            
            # Value is arbitrary, key needed to make sure no duplicates are written to file
            tweetIds[tweet['id_str']] = 1

            dataFile = open('dataFile.txt', 'a+')
            dataFile.write("\t" + formatUnicode(tweet['text'] + "\n\n"))
            
def getKeys():
    file = open("APIKeys.txt" , "r")
    
    accessToken = file.readline()
    accessToken = accessToken.strip('\n')
    
    accessTokenSecret = file.readline()
    accessTokenSecret = accessTokenSecret.strip('\n')
    
    consumerKey = file.readline()
    consumerKey = consumerKey.strip('\n')
    
    consumerSecret = file.readline()
    consumerSecret  = consumerSecret.strip('\n')
    
    return accessToken, accessTokenSecret, consumerKey, consumerSecret

def formatUnicode(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])    

main()