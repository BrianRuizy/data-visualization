
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

plt.show(sns.lmplot(x='Value', y='Overall', hue ='Position',
           data = footballers.loc[footballers['Position'].isin(['ST', 'CM', 'CB'])],
           fit_reg= False))

# Another example of a visual variable is 'shape', which controls marker shapes to help differentiate
sns.lmplot(x='Value', y='Overall', markers=['o', 'x', '*'], hue='Position',
           data=footballers.loc[footballers['Position'].isin(['ST', 'RW', 'LW'])],
           fit_reg=False
          )
