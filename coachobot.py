#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, datetime, random
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

today = datetime.date.today()
bamadate = datetime.date(2011, 11, 5)
diff = today - bamadate
dayssince = diff.days

encwords = ['You can totally do this.', 'Impossible is for the unwilling' , 'No pressure, no diamonds', 
'Take the risk or lose the chance' , 'Prove them wrong' , 'Make each day your masterpiece' , ' Tough times never last, but tough people do',
'Geaux tigers', 'STTDB', "Maybe take a team trip to Fred's?", "We comin' and we ain't backin' down", 'It is a pantheon of concrete and steel',
"Bogie's may have lost, but that doesn't mean we have too as well.", "Have you tried hiring Gordon McKernan?", "Maybe bring back the parade grounds...",
"Chance of rain? Never!", "Try asking Garth Brooks for advice", "Nick Saban is human too."]


message = "It has been " + str(dayssince) + " days since @LSUFootball has beaten the Crimson Tide in Football. @Coach_EdOrgeron " +  random.choice(encwords)

while True:
	timenow = time.strftime("%H:%M:%S", time.localtime())
	if timenow == '17:00:00':	
		print(message + "--------TWEETED AT TIME :" + time.strftime("%c"))
		api.update_status(message)
		print("waiting")
		time.sleep(5)
	else:
		time.sleep(5)
		print(timenow)

