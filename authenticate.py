#Authentication
from __future__ import absolute_import, print_function
import tweepy
import json

def authenticate(key_file='keys.json'):
        
    with open(key_file) as json_file:
        data = json.load(json_file)
        # == OAuth Authentication ==
        #
        # This mode of authentication is the new preferred way
        # of authenticating with Twitter.

        # The consumer keys can be found on your application's Details
        # page located at https://dev.twitter.com/apps (under "OAuth settings")
        consumer_key= data['Consumer_API_key'] or "" 
        consumer_secret=data['Consumer_API_Secret_key'] or ""

        # The access tokens can be found on your applications's Details
        # page located at https://dev.twitter.com/apps (located
        # under "Your access token")
        access_token=data['Access_token'] or ""
        access_token_secret=data['Access_token_secret'] or ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth

# If the authentication was successful, you should
# see the name of the account print out
if __name__ == "__main__":
    print('Hello',authenticate().me().name)



