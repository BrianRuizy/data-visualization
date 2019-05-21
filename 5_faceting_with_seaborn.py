import seaborn as sns
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('max_columns', None)
df = pd.read_csv("CompleteDataset.csv", index_col=0)


#  Data pre-processing ------------------------------------------------------------------------------
footballers = df.copy()
footballers['Unit'] = df['Value'].str[-1]
footballers['Value (M)'] = np.where(footballers['Unit'] == '0', 0,
                                    footballers['Value'].str[1:-1].replace(r'[a-zA-Z]',''))
footballers['Value (M)'] = footballers['Value (M)'].astype(float)
footballers['Value (M)'] = np.where(footballers['Unit'] == 'M',
                                    footballers['Value (M)'],
                                    footballers['Value (M)']/1000)
footballers = footballers.assign(Value=footballers['Value (M)'],
                                 Position=footballers['Preferred Positions'].str.split().str[0])
#  ---------------------------------------------------------------------------------------------------

df = footballers[footballers['Position'].isin(['ST', 'GK'])]
g = sns.FacetGrid(df, col='Position')  # Facet grid  is the main object used for breaking up visualization
plt.show(g)

#  After laying the grid we use 'map' object to plot corresponding data
df = footballers[footballers['Position'].isin(['ST', 'GK'])]
g = sns.FacetGrid(df, col='Position')
g.map(sns.kdeplot, 'Overall')
plt.show(g)

# Placing all the player positions on the facet grid
df = footballers
g = sns.FacetGrid(df, col = 'Position', col_wrap=6)
g.map(sns.kdeplot, 'Overall')
plt.show(g)

df = footballers[footballers['Position'].isin(['CM', 'CB'])]
df = df[df['Club'].isin(['Real Madrid CF', 'Juventus', 'Paris Saint-Germain', ''])]

g = sns.FacetGrid(df, row='Position', col='Club')
g.map(sns.violinplot, 'Overall')
plt.show(g)


