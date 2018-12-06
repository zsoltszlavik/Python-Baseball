import os
import re
import pandas as pd
import matplotlib.pyplot as plt

games_directory = os.path.join(os.getcwd(), 'games')
files = [fn for fn in os.listdir(games_directory) if fn.endswith(".EVE")]
files.sort()

event_rows = []
for file in files:
  with open(os.path.join(games_directory, file)) as current:
    for line in current:
      row = line.rstrip().split(',')

      if 'id' in row:
        id = row[1]

      # if 'visteam' in row:
      #   visteam = re.sub(r'\d', 'S', row[2])

      # if 'hometeam' in row:
      #   hometeam = re.sub(r'\d', 'S', row[2])

      if 'play' in row:
        row[0] = id

        # if row[2] == '0':
        #   row[2] = visteam
        # elif row[2] == '1':
        #   row[2] = hometeam

        event = row[-1].split('.')
        row.pop(-1)
        event_rows.append(row + event)

events = pd.DataFrame(event_rows)
events.columns = ['game_id', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'advancement']

strike_outs = events[events.event.str.contains('K')]

grouped_strike_outs = strike_outs.groupby(['game_id']).size()

strike_outs_game = grouped_strike_outs.reset_index(name='strike_outs')

year_strings = strike_outs_game.game_id.str.extract(r'^(?:N|A)LS(\d{4})', expand=False).values

year_values = pd.to_numeric(year_strings)

strike_outs_game = strike_outs_game.assign(year=year_values)

strike_outs_game = strike_outs_game.sort_values(by='year')

ax = strike_outs_game.plot(x='year', y='strike_outs')

ax.legend(['Strike Outs']);

plt.show()
