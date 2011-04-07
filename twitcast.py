#!/usr/bin/python

import os,sys
import time
import re
import twitter

delay = 900
api = twitter.Api()
last_tweet = ""
twit_source = 'kellymisa'

print "twitcast.py online"
while True:
    try:
        status = api.GetUserTimeline(twit_source)
        twit_user = status[0].user.name
        u = status[7].text.replace(u'\u201c','').replace(u'\u201d','').replace(u'\u2018','').replace(u'\u2019','').replace(u'\u263a','').replace(u'\u2665','').replace(u'\u2649','') # remove curly quotes, smiley, sad face and heart while in unicode
        twit = re.sub(r'(\'|\"|\@)','',str(u))
        if last_tweet != twit and len(twit) <= 140:		
            print " ".join([s for s in [twit_user,'says',twit]])
            os.system(" ".join([s for s in ['say -v Alex',twit_user,'says',twit]])) 
            last_tweet = twit
        print "waiting for next"
        time.sleep(delay)
    except (KeyboardInterrupt, SystemExit):
        exit()
    except:
        time.sleep(300)
        print "Retrying in 5 mins", sys.exc_info()[0]
