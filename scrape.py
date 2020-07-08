
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import urllib
from yurl import URL
import html2text
import spacy
import markdown2
import numpy as np
import os
import cfscrape

nlp = spacy.load('en_core_web_sm')

import json
from datetime import datetime, date
import re

def getSoup(url):
    scraper = cfscrape.create_scraper()
    content = scraper.get(url).content
    soup = BeautifulSoup(content, "html.parser")
    return soup

def getTopicRoots(forum_page):
    soup = getSoup(forum_page)
    titles = soup.findAll("h3", {"class": "title"})
    links = []
    orig_site = "/".join(forum_page.split("/")[:3]) + "/"
    for i in range(len(titles)):
        all_a = titles[i].findAll("a", href=True)
        for j in range(len(all_a)):
            links.append(orig_site + all_a[j]['href'])
    print(links)
    return links

def getAllTopicRoots(forum_pages):
    topic_roots = []
    for i in range(len(forum_pages)):
        topic_roots.append(getTopicRoots(forum_pages[i]))
    return topic_roots

def getTopicPages(topic_root):
    print(topic_root)
    soup = getSoup(topic_root)
    topic_pages = [topic_root]
    try:
        nav = soup.findAll('nav')[3]
        last_page = nav.text.split("\n")

        id = -1
        for i in range(len(last_page)):
            if "Next" in last_page[i]:
                id = i - 1

        if id == -1:
            exit()

        last_page = last_page[id]

        for i in range(2, int(last_page) + 1):
            topic_pages.append(topic_root + "page-" + str(i))
    except:
        print("One page topic")
    return topic_pages



def getForumPages(original_forum_url):
    soup = getSoup(original_forum_url)
    nav = soup.findAll('nav')[2]

    last_page = nav.text.split("\n")

    id = -1
    for i in range(len(last_page)):
        if "Next" in last_page[i]:
            id = i-1

    if id == -1:
        exit()

    last_page = last_page[id]

    forum_pages = [original_forum_url]
    for i in range(2, int(last_page)+1):
        forum_pages.append(original_forum_url + "page-" + str(i))

    return forum_pages

def getAllTopicPages(topic_roots):
    topic_pages = []
    for i in range(len(topic_roots)):
        all_topic_pages = []
        for j in range(len(topic_roots[i])):
            all_topic_pages.append(getTopicPages(topic_roots[i][j]))
        topic_pages.append(all_topic_pages)
    return topic_pages

def exists(filename, method, rewrite, params):
    if os.path.exists(filename) is False or rewrite is True:
        file = method(*params)
        np.save(filename, file)
    else:
        file = np.load(filename)
    return file


forum_pages = exists("data/forum_pages.npy", getForumPages, False, ["https://www.sythe.org/forums/runescape-2007-cheating/"])

topic_roots = exists("data/topic_roots.npy", getAllTopicRoots, False, [forum_pages])

topic_pages = exists("data/topic_pages.npy", getAllTopicPages, False, [topic_roots])





