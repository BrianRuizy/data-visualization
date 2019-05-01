import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('winemag-data_first150k.csv')  # storeed locally into project

print(reviews.head())

#  Scatter plot (lowly) down sampled
plt.show(reviews[reviews['price'] < 100].sample(300).plot.scatter(x='price', y='points'))

#  Hex plot
plt.show(reviews[reviews['price'] < 100].plot.hexbin(x='price', y='points', gridsize = 15))

#  Stack chart
wine_counts = pd.read_csv("winemag-data_first150k.csv", index_col=0)

print(wine_counts.head())

#  Stacked plots, much more visually informative
plt.show(wine_counts.plot.bar(stacked=True))
plt.show(wine_counts.plot.area())

#  Bivariate line chart
plt.show(wine_counts.plot.line())
