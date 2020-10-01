# tweepyScripts

Script will use Tweepy search API and user_time API. Adapted from this post: [Link](https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./)

# Overview

See individual script readmes for more details.

# Components

### twitterSearch

- Requires 3 arguments: searchterm (could be # hashtag, just put in quotes), number of Tweets to collect (some arbitrary large number), and filename to save as CSV output.

### twitterUserTimeline

- Requires a users.txt file to be in same directory which contains a list of all the usernames you want to download. See sample users.txt for example.
- Requires 2 arguments: max number of Tweets to collect (some arbitrary large number), and filename to save as CSV output.

### twitterUser

- No arguments, edit the users list with the username you want to search for and it will retreive various details about that user profile.

# Usage

- Assume Python is installed, pip install depenedencies (Tweepy, codecs, unicodecsv)
- Have a users.txt file located in the same folder.
- Run twitterUserTimeline.py with arguments, EX: "./twitterUserTimeline.py 10000 sampleOutput.csv"
- Run twitterSearch.py with arguments, EX: "./twitterSearch.py "#MarchMadness" 10000 sampleOutput.csv"
