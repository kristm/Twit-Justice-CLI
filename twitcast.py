#!/usr/bin/python

import os,sys
import time
import re
import twitter

delay = 900
api = twitter.Api()
last_tweet = ""
twit_source = 'lovipoe' #lovipoe, ina_feleo, kellymisa
#twit_source = 'kellymisa'
#twit_source = 'ina_feleo'

print "twitcast.py online"
while True:
    try:
        f = open('twitcast.log','a')
        status = api.GetUserTimeline(twit_source)
        twit_user = status[0].user.name
        #u = status[7].text.replace(u'\u201c','').replace(u'\u201d','').replace(u'\u2018','').replace(u'\u2019','').replace(u'\u263a','').replace(u'\u2665','').replace(u'\u2649','') # remove curly quotes, smiley, sad face and heart while in unicode
        twit = str("".join([c for c in status[0].text if ord(c) < 128])) # ignore non ascii characters
        twit = re.sub(r'(\'|\"|\@)|\)|\(|\-','',twit)
        if last_tweet != twit and len(twit) <= 140:		
            msg = " ".join([s for s in [twit_user,'says',twit,'\n']])
            print msg
            f.write(msg) 
            os.system(" ".join([s for s in ['say -v Alex',msg]])) 
            last_tweet = twit
            f.close()
        print "waiting for next"
        time.sleep(delay)
    except (KeyboardInterrupt, SystemExit):
        print "exiting"
        if not f.closed:
            f.close()
        exit()
    except (twitter.TwitterError):
        print "twitter error. retyring in 5 mins"
        time.sleep(delay)
    except:
        print "Retrying in 5 mins",sys.exc_info()[0]
        time.sleep(delay)

