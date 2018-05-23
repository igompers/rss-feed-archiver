#!/usr/bin/python
# rss-feed-archiver.py
# obvolvo . version 0.1

# load dependencies
import feedparser
import json

# get list of rss urls from file: rss_feed_source_list
def import_rss_feed_data():
    # import feeds from file
    rss_feed_source_list = []
    file = open('rss_feed_source_list', 'r')
    with open('rss_feed_source_list') as file:
        for x in file:
            rss_feed_source_list.append(x)
    file.closed

    # extract feed
    feeds = []
    for feed in rss_feed_source_list:
        feeds.append(feedparser.parse(feed))

    # lists for feed items
    url = []
    summary = []
    title = []

    # import items to lists
    feed_data_container = []
    for feed in feeds:
        for item in feed[ "items" ]:
            feed_data_container.append(item.link)
            feed_data_container.append(item.title)
            feed_data_container.append(item.summary)

    # return feed data
    return feed_data_container

# print feed items to console
# title, summary, link, etc.
def print_feed_items():
    # extract entries
    entries = []
    for feed in feeds:
        for item in feed[ "items" ]:
            entries.extend(item)

    feed_items = json.dumps(entries, file)
    print feed_items

# output feed data to file: exported_feed_data.json
def dump_feed_data(feed_data_container):
    # cast feed data as string
    feed_data = json.dumps(feed_data_container)

    # write feed data to file
    filename = 'exported_feed_data.json'
    if filename:
        with open(filename, 'w') as f:
            json.dump(feed_data, f)

# init.
def rss_feed_archiver_init():
    dump_feed_data(import_rss_feed_data())

rss_feed_archiver_init()
