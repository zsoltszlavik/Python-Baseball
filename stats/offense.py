import pandas as pd
import matplotlib.pyplot as plt

from data import games

# LO: Pandas selection (columns by label)
plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# LO: Pandas selection (rows and columns `loc`)
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

# LO: Pandas datatype conversion
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

# LO: Pandas replace values in column
replacements = {
  r'^S(.*)': 'single',
  r'^D(.*)': 'double',
  r'^T(.*)': 'triple',
  r'^HR(.*)': 'hr'
}

hit_type = hits['event'].replace(replacements, regex=True)

# LO: Pandas assign column to dataframe
hits = hits.assign(hit_type=hit_type)

# LO: Pandas group by column or columns
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')

# LO: Pandas enum
hits['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double', 'triple', 'hr'])

# LO: Pandas sorting by values
hits = hits.sort_values(['inning', 'hit_type'])

# LO: Pandas reshape `pivot`
hits = hits.pivot(index='inning', columns='hit_type', values='count')

# LO: Pandas plotting and plot formatting, specific plots
hits.plot.bar(stacked=True)

plt.show()
