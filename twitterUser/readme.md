# twitterUserInfo Script
Script will use Tweepy to download a users profile user_lookup API. Adapted from this post: [Link](https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./)

# Overview
This is a Python script that uses Tweepy to download user profile info user_lookup API.  Takes a list of users in the users.txt file (100 usernames/screennames, not user_ids, max) and will save all their profile info in csv format.  When the API limit is reached, it will sleep and wait for rate limit to pass then start collecting again.  Each time will append to the CSV filename you specify.

# Components
1. twitterUserInfo.py
  * Requires a users.txt file to be in same directory which contains a list of all the usernames/screenames you want to download (Must be usernames/screen_names not user_ids.  See sample users.txt for example.
  * Requires 1 argument: filename to save as CSV output.

# Usage
* Assume Python is installed, pip install depenedencies (Tweepy, codecs, unicodecsv)
* Have a users.txt file located in the same folder.
* Run twitterUserInfo.py with arguments, EX: "./twitterUserInfo.py sampleOutput.csv"
