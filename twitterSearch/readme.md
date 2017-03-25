# twitterSearch Script
Script will use Tweepy to search Twitter using hashtag serach api.  Adapted from this post: [Link](https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./)

# Overview
This is a Python script that uses Tweepy to search Twitter search API.  Will save tweets in csv format based on number you collect.  The programm will collect up to as many tweets as you specifiy in the 2nd argument paramter.  When the API limit is reached, it will sleep and wait for rate limit to pass then start collecting again.  Each time will append to the CSV filename you specify in 3rd argument.

# Components
1. twitterSearch.py
  * Requires 3 arguments: searchterm (could be # hashtag, just put in quotes), number of Tweets to collect (some arbitrary large number), and filename to save as CSV output.

# Usage
* Asusme Python is installed, pip install depenedencies (Tweepy, codecs, unicodecsv)
* Run twitterSearch.py with arguments, EX: "./twitterSearch.py "#MarchMadness" 100 march.csv"
