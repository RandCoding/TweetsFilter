from __future__ import absolute_import, print_function
from time import sleep
import json
from kafka import KafkaProducer

from tweepy import OAuthHandler, Stream, StreamListener
import authenticate as conn

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self,producer):
        self.producer = producer

    def on_data(self, data):
        val = json.loads(data)
        self.producer.send('test', value=val["created_at"])
        print(val)
        sleep(5)    
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda x: 
                            json.dumps(x).encode('utf-8'))

    tweets = StdOutListener(producer)

    stream = Stream(conn.authenticate('keys.json'), tweets)
    stream.filter(track=['tech'])


