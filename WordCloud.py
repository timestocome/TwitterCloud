
# http://github.com/timestocome
# read in any text and convert it to a word cloud


# uses https://github.com/amueller/word_cloud library


import datetime
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_current_wordcloud():

    # use today's date in image name
    today = datetime.date.today()
    image_name = 'tweetcloud_' + str(today.month) + '_' + str(today.day) + '.png'
   
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, 'cleaned_tweets.txt')).read()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # and save image as *.png
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(image_name)
   # plt.show()

    return image_name

#####################################################
generate_current_wordcloud()
