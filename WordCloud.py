#!/Users/ljcobb/anaconda/bin/python



# http://github.com/timestocome
# read in any text and convert it to a word cloud


# uses https://github.com/amueller/word_cloud library


import datetime
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt


path = os.path.dirname(os.path.realpath(__file__))


# today's file
today = datetime.date.today()
clean_file_name = path + '/cleaned_tweets_' + str(today.month) + '_' + str(today.day) + '.txt'



def generate_current_wordcloud():

    # use today's date in image name
    today = datetime.date.today()
    image_name = 'tweetcloud_' + str(today.month) + '_' + str(today.day) + '.png'
   

    # Read the whole text.
    text = open(clean_file_name).read()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # and save image as *.png
    plt.imshow(wordcloud)
    plt.axis("off")
    full_path = path + "/" + image_name
    plt.savefig(full_path)
   # plt.show()

    return image_name

#####################################################
#generate_current_wordcloud()
