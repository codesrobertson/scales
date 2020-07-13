# !/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pip(python 3.8)

from textblob import TextBlob

blob = "Gatsby is an absolutely amazing, lovable dog."
blob2 = "Donald Trump is the worst president." 

rating = TextBlob(blob).sentiment
rating2 = TextBlob(blob2).sentiment

print(rating)
print(rating2)
