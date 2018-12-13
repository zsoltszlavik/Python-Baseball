# 1 - ((H + ROE - HR) / (PA - BB - SO - HBP - HR))

import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games.query("type == 'play' & event != 'NP'")
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

pa = plays.loc[plays['player'].shift() != plays['player'], ['year', 'game_id', 'inning', 'team', 'player']]
pa = pa.groupby(['year', 'game_id', 'team']).size().reset_index(name='PA')

plays = plays.query("~(event.str.contains('^\d+') & ~event.str.contains('E'))")
plays = plays.query("~event.str.contains('^(?:P|C|F|I|O)')")

plays = plays.drop(['type', 'player', 'count', 'pitches'], axis=1)

plays = plays.sort_values(['team', 'inning']).reset_index()

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
plays = plays.assign(event_type=event_type)
plays = plays.groupby(['year', 'game_id', 'team', 'event_type']).size().reset_index(name='count')
plays = plays.set_index(['year', 'game_id', 'team', 'event_type'])
plays = plays.unstack()
plays = plays.fillna(0)
plays = plays.reset_index()
plays.columns = plays.columns.droplevel()
plays.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']
plays = plays.rename_axis(None, axis="columns")

plays = pd.merge(plays, pa, how='outer', left_on=['year', 'game_id', 'team'], right_on=['year', 'game_id', 'team'])

info = games.query("type == 'info' & (multi2 == 'visteam' | multi2 == 'hometeam')")
info = info.loc[:, ['year', 'game_id', 'multi2', 'multi3']]
info.columns = ['year', 'game_id', 'team', 'defense']

info.loc[info['team'] == 'visteam', 'team'] = '1'
info.loc[info['team'] == 'hometeam', 'team'] = '0'

info = info.sort_values(['year', 'game_id', 'team']).reset_index(drop=True)

plays = pd.merge(plays, info).drop(['team'], axis=1)

plays.loc[:, 'DER'] = 1 - ((plays['H'] + plays['ROE']) / (plays['PA'] - plays['BB'] - plays['SO'] - plays['HBP'] - plays['HR']))

plays['year'] = pd.to_numeric(plays['year'])

der = plays.loc[plays['year'] >= 1998, ['year', 'defense', 'DER']]

der = der.pivot(index='year', columns='defense', values='DER')

der.plot(x_compat=True, xticks=range(1998, 2018, 4), rot=45)

plt.show()