# 1 - ((H + ROE - HR) / (PA - BB - SO - HBP - HR))

import pandas as pd
import matplotlib.pyplot as plt

from data import games

der = games.query("type == 'play' & event != 'NP'")
der.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

pa = der.loc[der['player'].shift() != der['player'], ['year', 'game_id', 'inning', 'team', 'player']]
pa = pa.groupby(['year', 'game_id', 'team']).size().reset_index(name='PA')

der = der.query("~(event.str.contains('^\d+') & ~event.str.contains('E'))")
der = der.query("~event.str.contains('^(?:P|C|F|I|O)')")

der = der.drop(['type', 'player', 'count', 'pitches'], axis=1)

der = der.sort_values(['team', 'inning']).reset_index()

replacements = {
  r'^(?:S|D|T).*': 'H',
  r'^HR.*': 'HR',
  r'^W.*': 'BB',
  r'.*K.*': 'SO',
  r'^HP.*': 'HBP',
  r'.*E.*\..*B-.*': 'RO',
  r'.*E.*': 'E',
}

event_type = der['event'].replace(replacements, regex=True)
der = der.assign(event_type=event_type)
der = der.groupby(['year', 'game_id', 'team', 'event_type']).size().reset_index(name='count')
der = der.set_index(['year', 'game_id', 'team', 'event_type'])
der = der.unstack()
der = der.fillna(0)
der = der.reset_index()
der.columns = der.columns.droplevel()
der.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']
der = der.rename_axis(None, axis="columns")

der = pd.merge(der, pa, how='outer', left_on=['year', 'game_id', 'team'], right_on=['year', 'game_id', 'team'])

info = games.query("type == 'info' & (multi2 == 'visteam' | multi2 == 'hometeam')")
info = info.loc[:, ['year', 'game_id', 'multi2', 'multi3']]
info.columns = ['year', 'game_id', 'team', 'defense']

info.loc[info['team'] == 'visteam', 'team'] = '1'
info.loc[info['team'] == 'hometeam', 'team'] = '0'

info = info.sort_values(['year', 'game_id', 'team']).reset_index(drop=True)

der = pd.merge(der, info).drop(['team'], axis=1)

der.loc[:, 'der'] = 1 - ((der['H'] + der['ROE']) / (der['PA'] - der['BB'] - der['SO'] - der['HBP'] - der['HR']))

print(der)