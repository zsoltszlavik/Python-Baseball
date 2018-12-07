import pandas as pd
import matplotlib.pyplot as plt

from data import games

singles = games[(games.type == 'play') & games.event.str.startswith('S')]
doubles = games[(games.type == 'play') & games.event.str.startswith('D')]
triples = games[(games.type == 'play') & games.event.str.startswith('T')]
homeruns = games[(games.type == 'play') & games.event.str.startswith('HR')]

print(triples)


# strike_outs = strike_outs.groupby(['year', 'game_id']).size()
# strike_outs = strike_outs.reset_index(name='strike_outs')
# strike_outs = strike_outs[['year', 'strike_outs']].apply(pd.to_numeric)

# strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike Outs'])

# plt.show()