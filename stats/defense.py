# 1 - ((H + ROE - HR) / (PA - BB - SO - HBP - HR))

import pandas as pd
import matplotlib.pyplot as plt

from data import games

# LO: Pandas selection (rows by value `query`)
plays = games.query("type == 'play' & event != 'NP'")
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# LO: Pandas selection (rows and columns `loc`)
pa = plays.loc[plays['player'].shift() != plays['player'], ['year', 'game_id', 'inning', 'team', 'player']]

# LO: Pandas group by column or columns
pa = pa.groupby(['year', 'game_id', 'team']).size().reset_index(name='PA')

# LO: Pandas selection (rows by value `query`)
plays = plays.query("~(event.str.contains('^\d+') & ~event.str.contains('E'))")
plays = plays.query("~event.str.contains('^(?:P|C|F|I|O)')")

# LO: Pandas drop (columns by value `drop(axis=1)`)
plays = plays.drop(['type', 'player', 'count', 'pitches'], axis=1)

# LO: Pandas sorting by values
plays = plays.sort_values(['team', 'inning']).reset_index()

# LO: Pandas replace values in column
replacements = {
  r'^(?:S|D|T).*': 'H',
  r'^HR.*': 'HR',
  r'^W.*': 'BB',
  r'.*K.*': 'SO',
  r'^HP.*': 'HBP',
  r'.*E.*\..*B-.*': 'RO',
  r'.*E.*': 'E',
}
event_type = plays['event'].replace(replacements, regex=True)

# LO: Pandas assign column to dataframe
plays = plays.assign(event_type=event_type)

# LO: Pandas group by column or columns
plays = plays.groupby(['year', 'game_id', 'team', 'event_type']).size().reset_index(name='count')

# LO: Pandas indexing `set_index`
plays = plays.set_index(['year', 'game_id', 'team', 'event_type'])

# LO: Pandas reshape `unstack`
plays = plays.unstack()

# LO: Pandas fill empty 'cells' `fillna`
plays = plays.fillna(0)

# LO: Pandas indexing `reset_index`
plays = plays.reset_index()

# LO: Pandas indexing `droplevel` create by `unstack`
plays.columns = plays.columns.droplevel()

# LO: Pandas rename columns `rename_axis` create by `unstack`
plays.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']
plays = plays.rename_axis(None, axis="columns")

# LO: Pandas database like join `outer` on multiple columns
plays = pd.merge(plays, pa, how='outer', left_on=['year', 'game_id', 'team'], right_on=['year', 'game_id', 'team'])

# LO: Pandas selection (rows by value `query`)
info = games.query("type == 'info' & (multi2 == 'visteam' | multi2 == 'hometeam')")

# LO: Pandas selection (all rows and select columns `loc`)
info = info.loc[:, ['year', 'game_id', 'multi2', 'multi3']]
info.columns = ['year', 'game_id', 'team', 'defense']

# LO: Pandas change values `loc`
info.loc[info['team'] == 'visteam', 'team'] = '1'
info.loc[info['team'] == 'hometeam', 'team'] = '0'

# LO: Pandas sorting by values
info = info.sort_values(['year', 'game_id', 'team']).reset_index(drop=True)

# LO: Pandas database like join `outer` on multiple columns
plays = pd.merge(plays, info).drop(['team'], axis=1)

# LO: Pandas new column with calculated value
plays.loc[:, 'DER'] = 1 - ((plays['H'] + plays['ROE']) / (plays['PA'] - plays['BB'] - plays['SO'] - plays['HBP'] - plays['HR']))

# LO: Pandas datatype conversion
plays['year'] = pd.to_numeric(plays['year'])

# LO: Pandas selection (rows and columns `loc`)
der = plays.loc[plays['year'] >= 1998, ['year', 'defense', 'DER']]

# LO: Pandas reshape `pivot`
der = der.pivot(index='year', columns='defense', values='DER')

# LO: Pandas plotting and plot formatting
der.plot(x_compat=True, xticks=range(1998, 2018, 4), rot=45)

plt.show()