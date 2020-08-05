import tweepy
import time

#Set authentication parameters
auth = tweepy.OAuthHandler('er3koAlL1g0Ar0jgyt8WHzw17','KpFTn77xeQJFW8G46LWHCesEp1gLrOrB0fJnr4gyPX1sNQedtL')
auth.set_access_token('3237670278-VE77lhURXunlCUQ3r2Vjvwy3RdY12gneWRCIMkq','PnXupozXhRvBhZd1vuflXTTMADVxw3QbsuIrDN4a6t8V9')

#Set rate limit to avoid ban
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Get the user
user = api.me()
users_tweets = api.user_timeline(361961997)
tweets = api.home_timeline()

search = '#python'
#For a numerous hashtags, use a list
#search = ['#python','#javascript','#machinelearning']

#Pull 5 tweets
tweetnum = 5
tweetnum2 = 5

#Like tweets with specific hashtags
def like_tweets():
    for tweet in tweepy.Cursor(api.search, search).items(tweetnum):
        try:
            print("Tweet Liked")
            tweet.favorite()
            #Sleep to avoid instant likes and possible ban
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

#Like tweets of a specific user
def like_user_tweets():
    for tweet in tweepy.Cursor(api.user_timeline, screen_name='@elonmusk', tweet_mode="extended").items(tweetnum2):
        try:
            print("Elon's Tweet Liked")
            tweet.favorite()
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

like_tweets()
like_user_tweets()
