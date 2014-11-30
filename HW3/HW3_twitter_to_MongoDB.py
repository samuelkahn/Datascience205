"""
Using Twitter stream API, print all the tweets containing certain keywords in a 1 min period - reading the stream

"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from credentials import *
from time import time,ctime
import simplejson as json
import sys
from pprint import pprint as pp
import pymongo
### StdOutListiner inherits StreamListiner
class StdOutListener(StreamListener):
### Icreate new credit card instance 
### Define own instance variable timer 
    def __init__(self,timer):
        self.inc = 0
        StreamListener.__init__(self)
        # report the start of data collection...
        print "Gathering data at %s"%(str(ctime()))
        self.startTime = time()
        print "Start Time = %s"%(str(ctime()))
        ### When initialized, connects to MongoDB database tweets
        self.db=pymongo.MongoClient().tweets
        self.timer = timer
        self.count = 0

#### Overide on_data() method to handle the data how we want
#### THis method is caled every time raw data s recieved from connection
    def on_data(self, data):
        try:
            self.endTime = time()
            self.elapsedTime = self.endTime - self.startTime
            if self.elapsedTime <= self.timer:
                # load the JSON data
                data =json.loads(data[:-1])
                ### We inser each  JSON objec into MongoDB collection tweets_collections in database tweets
                self.db.tweets_collections.insert(data)
                #### +1 for each tweet
                self.count += 1

            else:
                ### Prints total tweets and elapsed time 
                print "Total Tweet Count== ",self.count
                print "End Time = %s"%(str(ctime()))
                print "Elapsed Time = %s"%(str(self.elapsedTime))

                return False
            return True
        except Exception, e:
            print e
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass
### Override on_error metho
    def on_error(self, status):
        print ("ERROR :",status)        
        
if __name__ == '__main__':
    ### Create stdOutListner Object 
    l = StdOutListener(60)
    ### Open the twitter 'fire hose'
    mystream = tweepy.Stream(auth, l, timeout=60)
    mystream.sample()



