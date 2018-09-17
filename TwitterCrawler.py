import sys
import tweepy
import urllib
import os
reload(sys)
sys.setdefaultencoding('utf-8')
PATH = "/Users/aznable/Desktop/"

#Set API
consumer_key = "ET7qvZgvkHliCUQ8pUe09SFev"
consumer_secret = "culgOtALdkW55Ox2oGVq6l5ypH53ChVoMq2eokyUnmARZKFAP0"
access_token = "1039253264775217152-S4QEuE2YyuTJ2OfUpuZjYMKqYo8ocm"
access_token_secret = "PoPrDFy8sd4TyAlNTLEqP6A97bpnNwt8Nadz1KH9hczaV"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Define how many following users you want to look through
user_number = 10

#Define how many recent tweets are used to summary
recent_number = 50

#Get following users
following = api.friends(count = user_number)

#Get images of each user
for i in range(0, len(following)):
    #Create file
    following_name = str(following[i].screen_name)
    file_path = PATH + following_name + "/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    #Get tweets
    tweets = api.user_timeline(following[i].id, count = recent_number)

    #Get image url for each tweet
    img_count = 0
    for j in range(0, len(tweets)):

        #Is retweet or not
        if hasattr(tweets[j], "retweeted_status") is True:
            ori_tweet = tweets[j].retweeted_status
        else:
            ori_tweet = tweets[j]

        media = tweets[j].entities.get("media")
        if media is not None:
            img_url = str(media[0].get("media_url_https"))
            img_count += 1

            #Save image to local files
            img_path = file_path + "image" + str(img_count) + ".jpg"
            urllib.urlretrieve(img_url, img_path)
