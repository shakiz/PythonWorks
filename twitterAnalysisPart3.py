import tweepy
from textblob import TextBlob

key='xKDWl0HfAqBuCRqE4caCFRcco'
secret='ayAfhyiLUHp3o5f9oMbIZvjyIkxCtbacCQeBAe161N5E4VYNkm'

token='2683935874-SEj83DJJwKMG4JkI9p7PAwORGOUzZmqsjiw3iQ8'
token_secret='UFjGSXCUWfMWUKUouTOvOii1bH5NeYgPSqFuCzYicEY5s'

auth=tweepy.OAuthHandler(key,secret)
auth.set_access_token(token,token_secret)

api=tweepy.API(auth)

for friend in tweepy.Cursor(api.friends).items():
    print(friend)

    
