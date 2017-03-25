# twitterUserTimeline Script
Script will use Tweepy to download a users' timeline using the user_timeline API.  Adapted from this post: [Link](https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./)

# Overview
This is a Python script that uses Tweepy to download user's timeline using user_timeline API.  Takes a list of users in the users.txt file and will save all their tweets in csv format.  By default it will collect the entire user's timeline as far back as possible which is typically ~3500 tweets.  When the API limit is reached, it will sleep and wait for rate limit to pass then start collecting again.  Each time will append to the CSV filename you specify.

# Components
1. twitterSearch.py
  * Requires a users.txt file to be in same directory which contains a list of all the usernames you want to download.  See sample users.txt for example.
  * Requires 2 arguments: max number of Tweets to collect (some arbitrary large number), and filename to save as CSV output.

# Usage
* Assume Python is installed, pip install depenedencies (Tweepy, codecs, unicodecsv)
* Have a users.txt file located in the same folder.
* Run twitterUserTimeline.py with arguments, EX: "./twitterUserTimeline.py 10000 sampleOutput.csv"
