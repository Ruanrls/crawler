#!/usr/bin/env python

##############    IMPORTS    ##############
try:
    import argparse#necessary to identify the args
    import re#necessary to the Regular expressions
    import requests#necessary to make requests from the dns host
    from random import choice
except ImportError as error:
    print "Impossible to import: " + str(error)

##############    PARSER    ##############

parser = argparse.ArgumentParser()
parser.add_argument("host", help="Host to makes a scan", action="store")
parser.add_argument('-v', '--verbose', help="Increase the verbosity", action='store_true', default=False)
parser.add_argument('-t', '--time', help="Defines the quantity of times that program will crawl (default 15)", type=int, default=15)
parser.add_argument('-r', '--randomize', help='Randomize the links to crawl', action='store_true')

arg = parser.parse_args()

##############    VARS    ##############

to_crawl = []
to_crawl.append(arg.host)

crawled = set()
email = set()

expressions = [r'href=[\"\'](https?://[\w]+\.[\w\.-_]+\.\w+[\.?\w+]?)[\'\"]', r'[\w\.-_]+@[\w\.-_]+\.com', r'[\w\.-_]+@[\w\.-_]+\.org']

##############    FUNCS    ##############

def crawler(link):
    global expressions
    global to_crawl
    global crawled

    try:
        ans = requests.get(link)
    except Exception as error:
        to_crawl.remove(link)
        if arg.verbose:
            print "Error to found the link: " + str(error)
        return

    html = ans.text#research the site html
    for each in expressions:#for each re
        finded = re.findall(each, html)#find all
        for ordene in finded:#for each result finded ordene in your respective list
            if '@' in ordene:
                email.add(ordene)
                if arg.verbose:
                    print "Email found: " + ordene
            else:
                if arg.verbose:
                    print "Link found: " + ordene
                if ordene not in to_crawl and ordene not in crawled:
                    to_crawl.append(ordene)
                    if arg.verbose:
                        print "The link is not crawled yet, adding: " + ordene

    crawled.add(link)#this link are crawled
    to_crawl.remove(link)#then we remove it

print "Crawling... "
for each in range(arg.time):
    if len(to_crawl) < 1:
        if arg.verbose:
            print "No more links"
        break

    if arg.randomize:
        crawler(choice(to_crawl))
    else:
        crawler(to_crawl[0])

if len(email) < 0 and len(crawled) < 0:
    print "No one link and emails founded!"
    exit()

if len(email) != 0:
    print "\nEmails: "
    for each in email:
        print each

if len(crawled) != 0:
    print "\nLinks: "
    for each in crawled:
        print each