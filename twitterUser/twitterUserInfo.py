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

# Filename
fName = sys.argv[1]

# List of users read from users.txt
users = []

#open users.txt file and gets the list of users
with open('users.txt', 'r') as f:
  for line in f:
    users.append(line.strip())

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
  print ("Can't Authenticate Bye!")
  sys.exit(-1)

with open(fName, 'ab') as f:
  writer = csv.writer(f, encoding='utf-8')
  writer.writerow(['Name','location','created_at','id_str','favourites_count','url','followers_count','time_zone','friends_count','screen_name'])

  try:      
    user_profiles = api.lookup_users(screen_names=users)
    
    if not user_profiles:
      print("No users found")
    
    for u in user_profiles:
      writer.writerow([u.name,u.location,u.created_at,u.id_str,u.favourites_count,u.url,u.followers_count,u.time_zone,u.friends_count,u.screen_name])

  except tweepy.TweepError as e:
    # Just exit if any error
    print("some error : " + str(e))
