# 1 - ((H + ROE - HR) / (PA - BB - SO - HBP - HR))

import pandas as pd
import matplotlib.pyplot as plt

from frames import games, info, events

# LO: Pandas selection (rows by value `query`)
plays = games.query("type == 'play' & event != 'NP'")
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# LO: Pandas selection (rows and columns `loc`)
pa = plays.loc[plays['player'].shift() != plays['player'], ['year', 'game_id', 'inning', 'team', 'player']]
# LO: Pandas group by column or columns
pa = pa.groupby(['year', 'game_id', 'team']).size().reset_index(name='PA')

# LO: Pandas indexing `set_index`
events = events.set_index(['year', 'game_id', 'team', 'event_type'])
# LO: Pandas reshape `unstack`
events = events.unstack().fillna(0).reset_index()
# LO: Pandas indexing `droplevel` create by `unstack`
events.columns = events.columns.droplevel()
# LO: Pandas rename columns `rename_axis` create by `unstack`
events.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']
events = events.rename_axis(None, axis="columns")

# LO: Pandas database like join `outer` on multiple columns
events_plus_pa = pd.merge(events, pa, how='outer', left_on=['year', 'game_id', 'team'], right_on=['year', 'game_id', 'team'])
# LO: Pandas database like join `outer` on multiple columns
defense = pd.merge(events_plus_pa, info)
# LO: Pandas new column with calculated value
defense.loc[:, 'DER'] = 1 - ((defense['H'] + defense['ROE']) / (defense['PA'] - defense['BB'] - defense['SO'] - defense['HBP'] - defense['HR']))
defense.loc[:, 'year'] = pd.to_numeric(defense['year'])
# LO: Pandas selection (rows and columns `loc`)
der = defense.loc[defense['year'] >=  1978, ['year', 'defense', 'DER']]
# LO: Pandas reshape `pivot`
der = der.pivot(index='year', columns='defense', values='DER')
# LO: Pandas plotting and plot formatting
der.plot(x_compat=True, xticks=range(1978, 2018, 4), rot=45)

plt.show()