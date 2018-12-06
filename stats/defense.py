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
