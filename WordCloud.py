#!/Users/ljcobb/anaconda/bin/python



# http://github.com/timestocome
# read in any text and convert it to a word cloud


# uses https://github.com/amueller/word_cloud library


import datetime
import time
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt




def generate_current_wordcloud(clean_file_name, image_name):

    # Read the whole text.
    text = open(clean_file_name).read()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # and save image as *.png
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(image_name)
  