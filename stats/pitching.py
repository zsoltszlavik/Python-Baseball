import pandas as pd
import matplotlib.pyplot as plt

from data import games

strike_outs = games[games.event.str.contains('K')]
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
strike_outs = strike_outs.reset_index(name='strike_outs')
strike_outs = strike_outs[['year', 'strike_outs']].apply(pd.to_numeric)

strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike Outs'])

plt.show()
