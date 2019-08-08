import json
from requests_oauthlib import OAuth1Session
import pandas as pd
import datetime
import time


def authentication():
    from requests_oauthlib import OAuth1Session
    import csv

    input_file = open('auth.csv', 'r', encoding="utf-8")
    reader = csv.DictReader(input_file)
    keys = [row for row in reader]
    input_file.close()

    return OAuth1Session(keys[0]["API_key"], keys[0]["API_secret"], keys[0]["Access_token"], keys[0]["Access_secret"])

def getTweets(twitter, lastId):
    url = "https://api.twitter.com/1.1/lists/statuses.json"

    if lastId == 0:
        params = {'list_id':1144937680683147267, 'count':200}
    else:
        params = {'list_id':1144937680683147267, 'count':200, 'since_id':lastId}
    return twitter.get(url, params=params)
    
    
def saveTweets(tweets):
    filename = 'json/tweets' + datetime.datetime.today().strftime('%m%d-%H%M') + '.json'
    f = open(filename, 'w', encoding='utf-8')
    json.dump(json.loads(tweets.text), f, ensure_ascii=False, indent=2)
    print(len(json.loads(tweets.text)))
    f.close()

def work(twitter, lastId):
    tweets = getTweets(twitter, lastId)
    if tweets.text != '[]':
        nextLastId = json.loads(tweets.text)[0]['id']
    else:
        nextLastId = lastId
    saveTweets(tweets)
    return nextLastId

#初期化
lastId = 0

while True:
    twitter = authentication()
    nextlastId = work(twitter, lastId)
    lastId = nextlastId
    print(datetime.datetime.now())

    time.sleep(600)
