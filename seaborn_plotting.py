import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

reviews = pd.read_csv("winemag-data_first150k.csv", index_col=0)

#  Pandas' bar chart = seaborn count plot
plt.show(sns.countplot(reviews['points']))

#  KDE plot (kernel density estimate)
#  similar to a line plot in pandas, however KDE addresses the issue with line charts on skewed data
plt.show(sns.kdeplot(reviews.query('price < 200').price))
plt.show(reviews[reviews['price'] < 200]['price'].value_counts().sort_index().plot.line())

#  Bivariate KDE plot
plt.show(sns.kdeplot(reviews[reviews['price'] < 200].loc[:, ['price', 'points']].dropna().sample(5000)))

#  Pandas histogram = seaborn distplot
plt.show(sns.distplot(reviews['points'], bins=10, kde=False))

#  Scatter plot, jointly
plt.show(sns.jointplot(x='price', y='points', data=reviews[reviews['price'] < 100]))

#  Hex plot, jointly
plt.show(sns.jointplot(
    x='price',
    y='points',
    data=reviews[reviews['price'] < 100], kind='hex',
    gridsize=20
))

# Box plot, great for summarizing shape of datasets of interval variables
df = reviews[reviews.variety.isin(reviews.variety.value_counts().head(5).index)]

plt.show(sns.boxplot(
    x = 'variety',
    y = 'points',
    data=df
))

#  Violin plot, functionally similar to boxplot, but employs KDE in place of the boxes
plt.show(sns.violinplot(
    x='variety',
    y='points',
    data=reviews[reviews.variety.isin(reviews.variety.value_counts()[:5].index)]
))

#  ----------------------------------------------------------------------------------------------

pokemon = pd.read_csv("Pokemon.csv", index_col=0)
plt.show(pokemon.head())

plt.show(sns.countplot(pokemon['Generation']))
plt.show(sns.distplot(pokemon['HP'], kde=True))
plt.show(sns.jointplot(x='Attack', y='Defense', data=pokemon))
plt.show(sns.kdeplot(pokemon['HP'], pokemon['Attack']))
plt.show(sns.boxplot(x='Legendary', y='Attack', data = pokemon))
plt.show(sns.violinplot(x='Legendary', y='Attack', data=pokemon))
