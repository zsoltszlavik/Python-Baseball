# 1 - ((H + ROE - HR) / (PA - BB - SO - HBP - HR))

# 1 - ((8 + 0 - 1) / (35 - 0 - 4 - 0 - 1))
import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games.query("type == 'play' & event != 'NP'")

plays.loc[plays.loc[:, 'game_id'] == 'ALS193307060']

# print(len(plays.loc[(plays.loc[:, 'game_id'] == 'ALS193307060') & (plays.loc[:, 'multi3'] == '0')]))


