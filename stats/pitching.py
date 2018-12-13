import pandas as pd
import matplotlib.pyplot as plt

from data import games

# LO: Pandas selection (rows by boolean)
plays = games[games['type'] == 'play']

# LO: Pandas selection (row by value `string contains`)
strike_outs = plays[plays['event'].str.contains('K')]

# LO: Pandas group by column or columns
strike_outs = strike_outs.groupby(['year', 'game_id']).size()

# LO: Pandas indexing `reset_index`
strike_outs = strike_outs.reset_index(name='strike_outs')

# LO: Pandas apply functions to multiple columns
strike_outs = strike_outs[['year', 'strike_outs']].apply(pd.to_numeric)

# LO: Pandas plotting and plot formatting `legend`
strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike Outs'])

plt.show()
