import os
import pandas as pd
import matplotlib.pyplot as plt

games_directory = os.path.join(os.getcwd(), 'games')

info_rows = []
start_rows = []
com_rows = []
play_rows = []
sub_rows = []
data_rows = []

with open(os.path.join(games_directory, '1933AS.EVE')) as file:
  for line in file:
    row = line.rstrip().split(',')
    if 'id' in row:
      id = row[1]
    elif 'version' in row:
      version = row[1]
    elif 'info' in row:
      info_rows.append(row)
    elif 'start' in row:
      start_rows.append(row)
    elif 'com' in row:
      com_rows.append(row)
    elif 'play' in row:
      play_rows.append(row)
    elif 'sub' in row:
      sub_rows.append(row)
    elif 'data' in row:
      data_rows.append(row)

info_frame = pd.DataFrame(info_rows)
start_frame = pd.DataFrame(start_rows)
com_frame = pd.DataFrame(com_rows)
play_frame = pd.DataFrame(play_rows)
sub_frame = pd.DataFrame(sub_rows)
data_frame = pd.DataFrame(data_rows)