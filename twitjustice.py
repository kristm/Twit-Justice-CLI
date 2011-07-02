#!/usr/bin/python

"""
twitjustice.py
Copyright (c) 2011, Krist Menina <krist@hellowala.org>

This code is free software; you can redistribute it and/or modify it under
the terms of the new BSD License.
"""
import os,sys
import time
import re
import twitter

def main():
    if len(sys.argv) < 2 :
        print "Usage: "+sys.argv[0]+" <twitter_username> [-d delay in seconds]"
        sys.exit(0)

    print sys.argv[0]+" online"

    delay = 900
    last_tweet = ""

    #define unicode constants
    HAPPY_FACE = u"\u263a"
    SAD_FACE = u"\u2639"
    YIN_YANG = u"\u262f"
    HEART = u"\u2665"

    api = twitter.Api()
    twit_source = sys.argv[1]
    if len(sys.argv) == 4 and sys.argv[2] == "-d" :
        mins = int(sys.argv[3])/60
        secs = int(sys.argv[3])%60
        print "set delay to "+str(mins)+"."+str(secs)+" minutes"
        delay = int(sys.argv[3])
    else:
        mins = delay/60
        secs = delay%60

    while True:
        try:
            f = open('twitjustice.log','a')
            status = api.GetUserTimeline(twit_source)
            twit_user = status[0].user.name
            msg = status[0].text
            msg = msg.replace(HAPPY_FACE,"smiley").replace(HEART,"heart")
            twit = str("".join([c for c in msg if ord(c) < 128])) # ignore non ascii characters
            twit = re.sub(r'(\'|\"|\@)|\)|\(|\-','',twit)
            if last_tweet != twit and len(twit) <= 140:		
                msg = " ".join([s for s in [twit_user,'says',twit,'\n']])
                print msg
                f.write(" ".join([s for s in [status[0].created_at,msg]])) 
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
            print "".join([s for s in ["twitter error. retrying in ",str(mins),".",str(secs)," mins"]])
            time.sleep(delay)
        except:
            print "".join([s for s in ["Retrying in ",str(mins),".",str(secs)," mins ",str(sys.exc_info()[0])]])
            time.sleep(delay)


if __name__ == "__main__":
    sys.exit(main())
