import re
import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games.loc[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

hits = plays.loc[plays.loc[:, 'event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

replacements = {
  r'^S(.*)': 'single',
  r'^D(.*)': 'double',
  r'^T(.*)': 'triple',
  r'^HR(.*)': 'hr'
}

hits.loc[:, 'inning'] = hits.loc[:, 'inning'].apply(pd.to_numeric)

hit_type = hits.loc[:, 'event'].replace(replacements, regex=True)

hits = hits.assign(hit_type=hit_type)

hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')

hits.loc[:, 'hit_type'] = pd.Categorical(hits.loc[:, 'hit_type'], ['single', 'double', 'triple', 'hr'])

hits = hits.sort_values(['inning', 'hit_type'])

hits = hits.pivot(index='inning', columns='hit_type', values='count')

hits.plot.bar(stacked=True)

plt.show()
