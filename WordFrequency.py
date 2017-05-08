#!/Users/ljcobb/anaconda/bin/python

# http://github.com/timestocome


############################################################################
# setup
#############################################################################
import numpy as np
import string as st 

from itertools import chain
import re
import os

from collections import Counter
from collections import OrderedDict 
import operator 


# use today's data
import datetime
today = datetime.date.today()
file_date = str(today.year) + '-' + str(today.month) + '-' + str(today.day)




path = os.path.dirname(os.path.realpath(__file__))
dir = '/saved_cleaned_tweets/'
files = []

dir_path = path + dir

for f in os.listdir(dir_path):
    if f.endswith(".txt"):
        files.append(f)


# read in each file and collect text
for f in files:

    # read in file, create name for output file
    file_location = path + dir + f 
    new_file_name = re.sub("cleaned_tweets_", "word_frequency_", f)
    print(new_file_name)

    file =  open(file_location, encoding='utf-8') 
    data = file.read()
    file.close()

    # combine lines, remove new line chars, convert to lower case
    data = data.replace("\\'", "'")
    data = data.replace("\\n", " ")
    data = data.lower()


    words = data.split()            # split into words
    words_set = set(words)          # unique words
    count = Counter(words)          # count words
    
    frequency = {}                  # create dictionary of word frequencies
    for k, v in count.items():
        frequency[k] = v 
    
    sorted_list = sorted(frequency.items(), key = operator.itemgetter(1), reverse=True)

    with open(new_file_name, 'w') as f:
        for i in sorted_list:
            row = "%s,%f\n" %(i[0], i[1])
            f.write(row)

    
