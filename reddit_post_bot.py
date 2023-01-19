# h3avren

import praw
import requests
from bs4 import BeautifulSoup


client_id = "ClientID"
client_secret = "ClientSecret"
user_agent = "Snoozilla Bot v3.3.3"
user_name = "Username"
passsword = "Password"

reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     username = username, password = password,
                     user_agent = user_agent)

subreddit = reddit.subreddit('Sub-RedditName')

title = ""
body = ""

subreddit.submit(title, selftext = body)

