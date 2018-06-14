from textblob import TextBlob
text = "Python is ok"
obj = TextBlob(text)
sentiment = obj.sentiment.polarity
print(sentiment)