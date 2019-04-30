import pandas as pd

# data set from Kaggle.com
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)


reviews.head(3)  # Showing first 3 rows

reviews['province'].value_counts().head(10).plot.bar()  # Bar charts & categorical data
# straight away, we can see the pattern in wine distribution, nominated by california

#  Will allow us to view the proportions categorically
(reviews['province'].value_counts().head(10) / len(reviews)).plot.bar()
#  We can now see that california produces about a third of market stock, as opposed to the more absolute data

reviews['points'].values().sort_index().plot.bar()

#  We then use a line chart, whereas a bar chart would show too many categories
reviews['points'].values().sort_index().plot.line()
#  The con being that it passes individual values, not effective when dealing with nominal data

#  Area charts are just line charts with the bottom colored, usually for visual representation
reviews['points'].value_counts().sort_index().plot.area()


