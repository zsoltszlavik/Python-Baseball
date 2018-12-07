import pandas as pd
import matplotlib.pyplot as plt

from data import events

strike_outs = events[events.event.str.contains('K')]
strike_outs = strike_outs.groupby(['game_id']).size()
strike_outs = strike_outs.reset_index(name='strike_outs')

years = strike_outs.game_id.str.extract(r'^(?:N|A)LS(\d{4})', expand=False).values
strike_outs = strike_outs.assign(year=years)
strike_outs = strike_outs.sort_values(by='year')

visual = strike_outs[['year', 'strike_outs']].apply(pd.to_numeric)

ax = visual.plot(x='year', y='strike_outs', kind='scatter')
ax.legend(['Strike Outs']);

plt.show()