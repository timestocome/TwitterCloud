#!/Users/ljcobb/anaconda/bin/python


# http://github.com/timestocome/
# build a markov chain and use it to predict Alice In Wonderland/Through the Looking Glass text


import numpy as np
import random
from collections import Counter
import datetime
import os

import markovify  # https://github.com/jsvine/markovify



#######################################################################
# read in text and break into words and sentences
#####################################################################




def markov_tweet(clean_file_name):


    # Read the whole text.
    data = open(clean_file_name).read()


    # create markov model
    model = markovify.Text(data, state_size=3)

    # generate text from model
    print("*******************************")
    generated_tweets = []
    for i in range(200):
        text = model.make_sentence()
        if text is not None:
            if len(text) < 140:
                generated_tweets.append(text)

    tweet = random.choice(generated_tweets)
    return tweet


# test function
#tweet = markov_tweet()
