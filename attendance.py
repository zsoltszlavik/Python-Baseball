import os
import pandas as pd
import matplotlib.pyplot as plt

games_directory = os.path.join(os.getcwd(), 'games')
files = [fn for fn in os.listdir(games_directory) if fn.endswith(".EVE")]
files.sort()

attendances = []
for file in files:
  with open (os.path.join(os.getcwd(), 'games', file), 'rt') as in_file:
    for line in in_file:
      row = line.rstrip().split(',')
      if 'attendance' in row:
        attendances.append([file, row[2]])

data = pd.DataFrame(attendances)
data.columns = ["year", "attendance"]

year = data.year.str.extract(r'^(\d{4})', expand=False)
data.year = pd.to_numeric(year)
data.attendance = pd.to_numeric(data.attendance)

data.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=data.attendance.mean(), label='Mean', linestyle='--', color='green')

plt.show()