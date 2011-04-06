#!/usr/bin/python

import os
import time
import twitter

delay = 900
api = twitter.Api()

print "twitcast.py online"
while True:
    try:
        status = api.GetUserTimeline('renanbarco')
        twit_user = status[0].user.name
        twit = status[0].text
        if len(twit) <= 140:		
            print " ".join([s for s in [twit_user,'says',twit]])
            os.system(" ".join([s for s in ['say -v Alex',twit_user,'says',twit]])) 
        print "waiting for next"
        time.sleep(delay)
    except (KeyboardInterrupt, SystemExit):
        exit()
    except:
        print "Retrying"
