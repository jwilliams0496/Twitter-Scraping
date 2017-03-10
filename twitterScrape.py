# File: twitterScrape.py
# Author: James Williams
# Date: 3/10/17

from twython import Twython

user_name = "JonTronShow"
hash_tag = "jontronshow"
search_type = 0 #0 for tweets from a hashtag, 1 for tweets from a user
search_size = 100

def main():
    f = open("APIKeys.txt" , "r")

    access_token = f.readline()
    access_token = access_token.strip('\n')
    
    access_token_secret = f.readline()
    access_token_secret = access_token_secret.strip('\n')
    
    consumer_key = f.readline()
    consumer_key = consumer_key.strip('\n')
    
    consumer_secret = f.readline()
    consumer_secret  = consumer_secret.strip('\n')

    print(access_token)
    print(access_token_secret)
    print(consumer_key)
    print(consumer_secret)

    print("Obtaining OAuth 2 token\n\n")

    twitter = Twython(consumer_key, consumer_secret, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()

    print("Access token granted\n")

    twitter = Twython(consumer_key, access_token=ACCESS_TOKEN)

    if (search_type == 1):
        user_timeline = twitter.get_user_timeline(screen_name=user_name)
        
        # And print the tweets for that user.
        for tweet in user_timeline:
            print(tweet['text'])

        
    if (search_type == 0):
        print("Searching for tweets\n")
        search = twitter.search(q=hash_tag, count=search_size)
        tweets = search['statuses']

        for tweet in tweets:
            print(tweet['id_str'], '\n', tweet['text'], '\n\n\n')
  
            print("\n\n\n*********", len(tweets), "**********\n\n\n")
            
main()