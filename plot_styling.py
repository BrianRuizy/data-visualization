#  Styling basics of plots
#  Going to be enhancing the visual cues of a simple bar plot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

reviews = pd.read_csv('winemag-data_first150k.csv', index_col=0)

print(reviews.head(3))

#  Compare to this with all default parameters
plt.show(reviews['points'].value_counts().sort_index().plot.bar())

#  Modified plotsize, color, fontsize, title
plt.show(reviews['points'].value_counts().sort_index().plot.bar(
    figsize=(12, 6),
    color='green',
    fontsize=18,
    title="Wine Mag Rankings"
))

ax = reviews['points'].value_counts().sort_index().plot.bar(
    figsize=(12, 6),
    color='mediumvioletred',
    fontsize=16
)
#  Title changes can't be done easily with Pandas, so will resort to matplotlib & Seaborn
ax.set_title("Rankings Given by Wine Magazine", fontsize=20)  # Title font change
sns.despine(bottom=True, left=True)  # Removal of black plot borders

plt.show(ax)

