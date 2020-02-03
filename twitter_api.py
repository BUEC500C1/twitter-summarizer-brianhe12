def print_feed(twitter_handle,numTweets):
    import tweepy
    import google_api
    from dotenv import load_dotenv
    import os

    load_dotenv()

    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

    api = tweepy.API(auth)

    # Print Twitter Feed of a User
    public_tweets = api.user_timeline(screen_name=twitter_handle, count=numTweets)

    # Images
    media_files = set()

    for tweet in public_tweets:
        print(tweet.text)
        media = tweet.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])

    print('---------------------------------\n')

    # Print all media and descriptions
    for media in media_files:
        print(media)
        google_api.detect_labels_uri(media)

    
