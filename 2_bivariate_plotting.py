import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('winemag-data_first150k.csv')  # stored locally into project
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

#  ----------------------------------------------------

pokemon = pd.read_csv("pokemon.csv", index_col=0)

print(pokemon.head())
plt.show(pokemon.plot.scatter(x='Attack', y='Defense'))

pokemon_stats_legendary = pokemon.groupby(['Legendary', 'Generation']).mean()[['Attack', 'Defense']]

plt.show(pokemon.plot.hexbin(x='Attack', y="Defense", gridsize=15))
plt.show(pokemon_stats_legendary.plot.hexbin(x='Attack', y='Defense', gridsize=15))
plt.show(pokemon_stats_legendary.plot.bar(stacked=True))
pokemon_stats_by_generation = pokemon.groupby('Generation').mean()[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
plt.show(pokemon_stats_by_generation.plot.line())
