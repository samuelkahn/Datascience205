# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 15:23:14 2014

@author: samuel
"""

import simplejson as json
import pymongo
import nltk
import matplotlib.pyplot as plt
import numpy as np
import re
### This object interacts with MongoDB
class MongoDB_tweets():
    def __init__(self):
        ### When initialized, connects to MongoDB database tweets
        self.db=pymongo.MongoClient().tweets
        ### List of tweets will contain all the term
        self.list_of_tweets=[]
        ### Counter for keeping track of how any ascii and nonascii tweets
        self.ascii_tweets=0
        self.non_ascii_tweets=0
        ### Dictinary to hold most frequet terms
        self.most_frequent={}
### Get the tweets
    def get_collection_of_tweets(self):
        ### get the MongoDB collection in database tweets
        collection_of_tweets=self.db.tweets_collections
        ### Loop over each documet in collectin
        for document in collection_of_tweets.find():
            try:
                ### This creates on long list of term (only ASCII)
                self.list_of_tweets.extend(document['text'].decode('ascii').split())
                self.ascii_tweets+=1
            except KeyError as keyerror:
                pass
            except UnicodeDecodeError as unierror:
                self.non_ascii_tweets+=1
        ### All words are lower case
        self.list_of_tweets=[word.lower() for word in self.list_of_tweets]
        print 'There are '+str(self.ascii_tweets)+' ASCII tweets'
        print 'There are '+str(self.non_ascii_tweets)+' Non-ASCII tweets'
### Most frequent terms    
    def get_most_frequent_terms(self,numberofterms):
        frequency_distribution= nltk.FreqDist(self.list_of_tweets).items()
#        fifty_most_common=frequency_distribution[0:numberofterms]
        ### Put the N most frequent term into dictioary 
        for x in range(0,len(frequency_distribution)):
            if re.match(r"[-.,!?;]",frequency_distribution[x][0]):
                continue
            self.most_frequent[str(frequency_distribution[x][0])]=float(frequency_distribution[x][1])
            if len(self.most_frequent.keys())==50:
                break
#### Plot the distibution of most frequent terms
    def plot_dist_of_term(self):
        ## Creat arrays and sort the keys and values in descending order
        keys=np.array(self.most_frequent.keys())
        values=np.array(self.most_frequent.values())
        keys=keys[values.argsort()[::-1]]
        values=values[values.argsort()[::-1]]
        
        ind=np.arange(len(keys))
        width = 0.35 
        ### Plot the histogram useing a barplot
        plt.bar(ind, values,width)
        plt.xticks(ind+width/2., keys, rotation=90,size=9)
        plt.xlabel('Counts')
        plt.ylabel('Terms')
        plt.title('The '+str(len(keys))+' Most Frequent Terms')
        plt.show()
if __name__ == '__main__':
    tweets=MongoDB_tweets()
    tweets.get_collection_of_tweets()
    tweets.get_most_frequent_terms(50)
    tweets.plot_dist_of_term()
