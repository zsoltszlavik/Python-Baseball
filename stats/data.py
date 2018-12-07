import os
import glob
import pandas as pd

games_directory = os.path.join(os.getcwd(), 'games')
event_files = glob.glob(os.path.join(games_directory, '*.EVE'))
event_files.sort()

info_rows = []
event_rows = []
for event_file in event_files:
    current = open(event_file, 'r')
    for line in current:
        row = line.rstrip().split(',')

        if 'id' in row:
            id = row[1]

        if 'info' in row:
            row[0] = id

            info_rows.append(row)

        if 'play' in row:
            row[0] = id

            event = row[-1].split('.')
            row.pop(-1)
            event_rows.append(row + event)

    current.close()

events = pd.DataFrame(event_rows)
events.columns = ['game_id', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'advancement']

info = pd.DataFrame(info_rows)
info.columns = ['game_id', 'key', 'value']