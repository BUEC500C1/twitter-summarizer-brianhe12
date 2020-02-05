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

    print('\033[95m' + '@' + twitter_handle + '\033[0m')
    for tweet in public_tweets:
        media = tweet.entities.get('media', [])
        print(tweet.text)
        if len(media):
            print('\033[95m' + media[0]['media_url'] + '\033[0m')
            google_api.detect_labels_uri(media[0]['media_url'])
        print('\033[92m' + '----------' + '\033[0m')

    
