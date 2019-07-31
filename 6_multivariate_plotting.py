
import pandas as pd

pd.set_option('max_columns', None)
df = pd.read_csv("Fifa18Dataset.csv", index_col=0)

import re
import numpy as np

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

print(footballers.head())

# We will be adding more visual variables to help perceptually distinguish data elements
# Starting with multivarite scatterplot

import seaborn as sns
import matplotlib.pyplot as plt
'''
# comparing value / wage to overall rating of 3 different player positions [st, cm, cb]
# using visual variable of 'color' to distinguish differences
plt.show(sns.lmplot(x='Value', y='Overall', hue ='Position',
           data = footballers.loc[footballers['Position'].isin(['ST', 'CM', 'CB'])],
           fit_reg= False))

# another visual element for the plots include modifying the markers 'shape'
# though, typically color is a better differentiator than shape
sns.lmplot(x='Value', y='Overall', markers=['o', 'x', '*'], hue='Position',
           data=footballers.loc[footballers['Position'].isin(['ST', 'RW', 'LW'])],
           fit_reg=False
          )
'''
# A good comparison demonstrative plot is the 'grouped box plot'
# I.e. we want to explore to find what position players score higher in 'aggression' attribute

f = (footballers.loc[footballers['Position'].isin(['ST', 'CB'])]
                .loc[:, ['Value', 'Overall', 'Aggression', 'Position']])

f = f[f["Overall"] >= 80]
f = f[f["Overall"] < 85]
f['Aggression'] = f['Aggression'].astype(float)

plt.show(sns.boxplot(x="Overall", y="Aggression", hue='Position', data=f))

# We see how useful a box plot can be, however when we want to compare even more dimensions of data
# we affect the interpretability of the plots by making them busier.
# A solution to this would be summarization plots, an example of one is a 'heatmap' / 'correlation plot'

f = (footballers.loc[:, ['Acceleration', 'Aggression', 'Agility', 'Balance', 'Ball control']]
                .applymap(lambda v: int(v) if str.isdecimal(v) else np.nan)
                .dropna()).corr()

plt.show(sns.heatmap(f, annot = True))
# Here we can now see correlations between different attributes and their

