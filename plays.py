import os
import pandas as pd
import matplotlib.pyplot as plt

games_directory = os.path.join(os.getcwd(), 'games')
files = [fn for fn in os.listdir(games_directory) if fn.endswith(".EVE")]
files.sort()

play_rows = []
for file in files:
  with open(os.path.join(games_directory, file)) as current:

    for line in current:
      row = line.rstrip().split(',')
      if 'id' in row:
        id = row[1]

      if 'play' in row:
        row.insert(1, id)
        play_rows.append(row)

play_frame = pd.DataFrame(play_rows).drop(0, axis=1)
print(play_frame)