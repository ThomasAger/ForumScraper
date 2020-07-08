from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import urllib
from yurl import URL
import markdown2
import numpy as np
import os
import cfscrape
import util as u
import json
from datetime import datetime, date
import re


urls = np.load("data/urls/topic_pages.npy")
all_posts = []
# For each page of topics
for i in range(len(urls)):
    topic_messages = []
    # Get the topic
    for j in range(len(urls[i])):
        page_messages = []
        # For each page of posts
        for k in range(len(urls[i][j])):
            # Get the page of posts and convert to CSV
            soup = u.getSoup(urls[i][j][k])
            names = soup.findAll("li", {"class": "message"})
            text_names = []
            for n in range(len(names)):
                text_names.append(names[n]["data-author"])
            messages = soup.findAll("blockquote", {"class": "messageText"})
            text_messages = []
            for n in range(len(messages)):
                text_messages.append(messages[n].text)
            print(i, "/", len(urls),  j, "/", len(urls[i]), k, "/",  len(urls[i][j]), text_messages)
            page_messages.append(text_messages)
        topic_messages.append(page_messages)
    all_posts.append(topic_messages)

np.save("data/text/all_posts.npy", all_posts)