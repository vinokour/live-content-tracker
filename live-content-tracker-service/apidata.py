
import json
from pip._vendor import requests
from datetime import datetime, timezone

from zoneinfo import ZoneInfo

def convert_user_date_to_start_time(date):
    user_tz = ZoneInfo("America/New_York")
    start_date_ny = date.replace(tzinfo = user_tz, hour=0, minute=0, second=0)
    start_date_utc = start_date_ny.astimezone(timezone.utc)
    return(start_date_utc.strftime('%Y-%m-%dT%H:%M:%SZ'))
    


def convert_user_date_to_end_time(date):
    user_tz = ZoneInfo("America/New_York")
    end_date_ny = date.replace(tzinfo = user_tz, hour=23, minute=59, second=59)
    end_date_utc = end_date_ny.astimezone(timezone.utc)
    return(end_date_utc.strftime('%Y-%m-%dT%H:%M:%SZ'))
    
    
   
 
def get_userID(account):
    url= 'https://api.twitter.com/2/users/by/username/{}'.format(account)
    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAK%2f%2feAEAAAAADblf7cPVVJ1WQ2TN8HwycbfBm8U%3DRWG76n3mzSIoUssth3uxY9IOE8kH4IV2Sgt4iFtYex68MWUG6F'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['data']['id']
def get_twitter_username(userId):
    url = 'https://api.twitter.com/2/users/{}?user.fields=username'.format(userId)
    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAK%2f%2feAEAAAAADblf7cPVVJ1WQ2TN8HwycbfBm8U%3DRWG76n3mzSIoUssth3uxY9IOE8kH4IV2Sgt4iFtYex68MWUG6F'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['data']['username']

def get_twitter_post_data(userId,date):
    url = 'https://api.twitter.com/2/users/{}/tweets?start_time={}&end_time={}&exclude=retweets,replies&max_results=100&expansions=attachments.media_keys&media.fields=url,height,width,preview_image_url,public_metrics&tweet.fields=public_metrics,created_at'.format(userId,convert_user_date_to_start_time(date), convert_user_date_to_end_time(date))
    headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAK%2f%2feAEAAAAADblf7cPVVJ1WQ2TN8HwycbfBm8U%3DRWG76n3mzSIoUssth3uxY9IOE8kH4IV2Sgt4iFtYex68MWUG6F'}
    response = requests.get(url, headers=headers)
    data = response.json() 
    return data
def sort_data_2(tweets_response,account):
    tweets = []
    media = index_attachments_by_media(tweets_response['includes']['media'])
    
    for tweet in tweets_response['data']:
        if 'attachments' not in tweet:
            continue

  
        attachments = []

        for media_key in tweet['attachments']['media_keys']:
            attachments.append(media[media_key])
        tweet["attachments"] =  attachments
        #switch date from 'created_at' of the format '2020-04-01T00:00:00Z' to -'yyyy-mm-dd'
        tweet["created_at"] = tweet["created_at"].split('T')[0]
        tweet['username'] = account
        
       
        
    
        tweets.append(tweet)
    
    
    return tweets
        



def index_attachments_by_media(attachments):
    media={}
    for attachment in attachments:
        media[attachment["media_key"]]= attachment
    return media

      

data = get_twitter_post_data(get_userID('mlb'),datetime(2022,7,26))









data_list = sort_data_2(data,'mlb')
yo=sort_data_2(get_twitter_post_data(get_userID('mlbjapan'),datetime(2022,7,26)),'mlbjapan')
print(yo)



#data_list.append(sort_data(get_twitter_post_data(get_userID('lasmayores'),datetime(2022,7,22)),'lasmayores'))
#data_list.append(sort_data(get_twitter_post_data(get_userID('mlbjapan'),datetime(2022,7,22)),'mlbjapan'))
#data_list.append(sort_data(get_twitter_post_data(get_userID('mlbdominicana'),datetime(2022,7,22)),'mlbdominicana'))
#data_list.append(sort_data(get_twitter_post_data(get_userID('mlbcuba'),datetime(2022,7,22)),'mlbcuba'))
#data_list.append(sort_data(get_twitter_post_data(get_userID('mlbvenezuela'),datetime(2022,7,22)),'mlbvenezuela'))
#data_list.append(sort_data(get_twitter_post_data(get_userID('mlbmexico'),datetime(2022,7,22)),'mlbmexico'))
#data_list.append(sort_data(get_twitter_post_data(get_userID('mlbpuertorico'),datetime(2022,7,22)),'mlbpuertorico'))




