import os
import re
import pandas as pd
import matplotlib.pyplot as plt

games_directory = os.path.join(os.getcwd(), 'games')
files = [fn for fn in os.listdir(games_directory) if fn.endswith(".EVE")]
files.sort()

play_rows = []
for file in files:
  with open(os.path.join(games_directory, file)) as current:
    year = file.replace('AS.EVE', '')
    for line in current:
      row = line.rstrip().split(',')
      if 'id' in row:
        id = row[1]

      if 'play' in row:
        row[0] = id
        row.insert(1, year)
        event = row[-1].split('.')
        row.pop(-1)
        play_rows.append(row + event)

play_frame = pd.DataFrame(play_rows)
play_frame.columns = ['game_id', 'year', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'advancement']

print(play_frame)
# with pd.option_context('display.max_rows', None):
#   print(play_frame.query("game_id == 'NLS201807170' and team == '0' and (event.str.startswith('HR') or advancement.str.contains('H'))"))
#   print(play_frame.query("event.str.startswith('K')").groupby('year').size())
