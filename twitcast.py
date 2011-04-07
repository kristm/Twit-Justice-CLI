#!/usr/bin/python

import os,sys
import time
import twitter

delay = 900
api = twitter.Api()
last_tweet = ""

print "twitcast.py online"
while True:
    try:
        status = api.GetUserTimeline('renanbarco')
        twit_user = status[0].user.name
        twit = str(status[0].text.decode('utf-8')).replace('\'','')
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
