import tweepy
from textblob import TextBlob

api_key='xKDWl0HfAqBuCRqE4caCFRcco'
api_secret='ayAfhyiLUHp3o5f9oMbIZvjyIkxCtbacCQeBAe161N5E4VYNkm'

token='2683935874-SEj83DJJwKMG4JkI9p7PAwORGOUzZmqsjiw3iQ8'
token_secret='UFjGSXCUWfMWUKUouTOvOii1bH5NeYgPSqFuCzYicEY5s'

authentication=tweepy.OAuthHandler(api_key,api_secret)
authentication.set_access_token(token,token_secret)

api=tweepy.API(authentication)

print('Enter text to get analysis:')
tweetText=raw_input()

sTweet=api.search(tweetText)

for t in sTweet:
    print(t.text)
    analysis=TextBlob(t.text)
    print(analysis.sentiment)

user=api.get_user('twitter')

try:
    print(user.screen_name)
    print(user.followers_count)

    for frnd in user.friends():
        print(frnd.screen_name)
except tweepy.TweepError as e:
    print(getExceptionMessage(e.reason))
