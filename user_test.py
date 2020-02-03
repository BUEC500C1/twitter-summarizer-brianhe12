import google_twitter_api 

def test():
    try:
        google_twitter_api.api_print("FloodSocial",10)
        assert True
    except:
        assert False