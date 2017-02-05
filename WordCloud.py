
# http://github.com/timestocome
# read in any text and convert it to a word cloud


# uses https://github.com/amueller/word_cloud library


from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)


# Read the whole text.
text = open(path.join(d, 'cleaned_tweets.txt')).read()


# Generate a word cloud image
wordcloud = WordCloud().generate(text)


# Display the generated image:
# and save image as *.png
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("tweetcloud.png")

plt.show()

