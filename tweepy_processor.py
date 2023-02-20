import tweepy
from tw_sentiment import TwSentiment

import tw_credentials

max_tweets_to_analyze = 100

#Class for streaming and process tweets
class TwitterStreamer():
    def analyze_tweets(self, api, hashtag):
        results = []

        analizer = TwSentiment()
            
        for tweet in tweepy.Cursor(api.search, q=hashtag, tweet_mode='extended').items(max_tweets_to_analyze):
            #Pass the first row, as the first row is the header
            results.append(analizer.do_analize(tweet._json['full_text']))
            
        return results

#Class a basic listener class that prints tweets to stdout
class StdOutListener(tweepy.Stream):    
    def setFilenameOutput(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self, data):
        try:
            print(data)
            with open (self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True
    
    def on_error(self, status):
        #In case of rate limit occurs
        if status == 420:
            return False
        print(status)
    
#Class for analyzing and categorizing content from tweets    
class TweetAnalyzer():
    pass
        
if __name__ == "__main__":
    auth = tweepy.OAuthHandler(tw_credentials.CONSUMER_KEY, tw_credentials.CONSUMER_SECRET)    
    auth.set_access_token(tw_credentials.ACCESS_TOKEN, tw_credentials.ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    hash_tag_list = ['covid19']
    
    twStreamer = TwitterStreamer()
    
    twStreamer.analyze_tweets(api, hash_tag_list)