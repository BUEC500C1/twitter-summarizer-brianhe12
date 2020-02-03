import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)

# Print Twitter Feed of a User
public_tweets = api.user_timeline(screen_name="FloodSocial", count=200)

# Images
media_files = set()

for tweet in public_tweets:
    print(tweet.text)
    media = tweet.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

print('---------------------------------')

# Print all media
for media in media_files:
    print(media)
