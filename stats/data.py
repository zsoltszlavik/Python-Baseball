import os
import glob
import pandas as pd

# LO: Python File management
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
game_files.sort()

game_frames = []
for game_file in game_files:
    # LO: Pandas Read CSV Data
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3',
                                               'multi4', 'multi5', 'multi6',
                                               'event'])
    game_frames.append(game_frame)

# LO: Pandas appending data frames
games = pd.concat(game_frames)

# LO: Pandas change values `loc`
games.loc[games['multi5'] == '??', 'multi5'] = ''

# LO: Pandas string methods (extract)
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

# LO: Pandas fill empty 'cells' `fillna` with forward fill
identifiers = identifiers.fillna(method='ffill')

# LO: Pandas `columns` property
identifiers.columns = ['game_id', 'year']

# LO: Pandas appending data frames
games = pd.concat([games, identifiers], axis=1, sort=False)

# LO: Pandas fill empty 'cells' `fillna`
games = games.fillna(' ')

# LO: Pandas enum
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])