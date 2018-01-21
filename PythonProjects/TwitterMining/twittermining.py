import tweepy
from tweepy import OAuthHandler

from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = '1zlbhPITIs4tr16ilTIwOSwvh'
consumer_secret = 'LXa7RDRBA6QHaud3WekFhl24qcaBzpcLcy7OP7oKDJ8jHtoCvB'
access_token = '73121960-V0GDbnFdifcfNvLW7A4cBbodpE8jCd2zHS3VCeJb6'
access_secret = 'NZ8y7AKvNcGKwSaOS4K2ePp0otq5JlsVrNILCP7p5FEIw'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

for friend in tweepy.Cursor(api.friends).items():
    # Process a single status
    print(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


class MyListener(StreamListener):
    
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])

