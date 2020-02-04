# twitter-summarizer-brianhe12
Module with an API that will return to the user of the API in text the twitter feed summary (Twitter Feeds and text description of the images).

### Built with:

[Tweepy](http://docs.tweepy.org/en/latest/#)

[Google Vision API](https://cloud.google.com/vision)

We have one method that receives a person's Twitter handle and an integer value indicating the number of recent tweets the user of the API wants to display.
```python
api_print(twitter_handle,numTweets)
```

### Try it Out!
Clone this repository and authenticate with [Tweepy](http://docs.tweepy.org/en/latest/#) and [Google Vision API](https://cloud.google.com/vision).

#### Tweepy 
For [Tweepy](http://docs.tweepy.org/en/latest/#), you will need to create a [.env](https://pypi.org/project/python-dotenv/) file with your own generated keys for authentication. 

#### Google Vision API
For [Google Vision API](https://cloud.google.com/vision), you will need to enable the Google Vision API and create a service account. For more information, look at the Quickstart guide [here](https://cloud.google.com/vision/docs/setup).

### Example Usage
```python
# user.py
import google_twitter_api 

google_twitter_api.api_print("kobebryant",10)
```
This function call will print out the 10 most recent tweets of [@kobebryant](https://twitter.com/kobebryant) and use Google's Vision API to analyze any images in those tweets.

### Example Output
<img src = "example_output.JPG">
