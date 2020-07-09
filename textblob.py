from textblob import TextBlob

blob = "Gatsby is an absolutely amazing, lovable dog."
blob2 = "Donald Trump is the worst president." 

rating = TextBlob(blob).sentiment
rating2 = TextBlob(blob2).sentiment

print(rating)
print(rating2)
