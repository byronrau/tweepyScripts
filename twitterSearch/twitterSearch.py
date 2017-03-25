#!/usr/bin/python
import tweepy
import sys
import os
import codecs
import unicodecsv as csv

# API and ACCESS KEYS
API_KEY = 'jz3feMK2gN0kaN377FsTXY7uY'
API_SECRET = 'sGfCEayfwORloC9SvHy6BmDjifUsUEIF0EF51SgiYUgs054n7H'

# Don't buffer stdout, so we can tail the log output redirected to a file
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# Search term to find
searchQuery = sys.argv[1]

# Max Tweets
maxTweets = int(sys.argv[2])

# Tweets per Query
tweetsPerQry = 200

# Filename
fName = sys.argv[3]

# To track last tweet ID collected
sinceId = None

if(len(sys.argv) > 4):
  if(sys.argv[4] != '-1'):
    sinceId = sys.argv[4]

# Specifiy last ID to start search from
last_id = -1L

if(len(sys.argv) > 5):
  last_id = long(sys.argv[5])

def getHashtags(hashes):
  hashStr = ''
  for i, h in enumerate(hashes):
    if i == len(hashes)-1:
      hashStr = hashStr + h['text']
    else:
      hashStr = hashStr + h['text'] + ','
  return hashStr

def getMentions(mentions):
  mentionStr = ''
  for i, m in enumerate(mentions):
    if i == len(mentions)-1:
      mentionStr = mentionStr + m['screen_name']
    else:
      mentionStr = mentionStr + m['screen_name'] + ','
  return mentionStr

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
  print ("Can't Authenticate Bye!")
  sys.exit(-1)

tweetCount = 0

print("Downloading max {0} tweets".format(maxTweets))

with open(fName, 'ab') as f:
  writer = csv.writer(f, encoding='utf-8')
  writer.writerow(['Username','Created_at','ID','Text','RetweetCount','Name','Location','URL','Description','TweetCount','FollowersCount','FriendsCount','Hashtags','mentions'])
  tweetCount = 0
  last_id = 0

  while tweetCount < maxTweets:
    try:
      if (last_id <= 0):
        if (not sinceId):
          new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
        else:
          new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since_id=sinceId)
      else:
        if (not sinceId):
          new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(last_id - 1))
        else:
          new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(last_id - 1), since_id=sinceId)

      if not new_tweets:
        print("No more tweets found")
        break
    
      for tweet in new_tweets:
        hashTags = getHashtags(tweet.entities.get('hashtags'))
        mentions = getMentions(tweet.entities.get('user_mentions'))

        writer.writerow([tweet.user.screen_name,tweet.created_at,tweet.id_str,tweet.text,str(tweet.retweet_count),tweet.user.name, tweet.user.location, str(tweet.user.url),tweet.user.description,str(tweet.user.statuses_count),str(tweet.user.followers_count),str(tweet.user.friends_count),hashTags,mentions])

      tweetCount += len(new_tweets)
      print("Downloaded {0} tweets".format(tweetCount))
      last_id = new_tweets[-1].id
    
    except tweepy.TweepError as e:
      # Just exit if any error
      print("some error : " + str(e))
      break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))