import google_twitter_api 

def test():
    try:
        import tweepy
        from google.cloud import vision
        assert True
    except:
        assert False