import pandas as pd
import matplotlib.pyplot as plt

from data import info

attendance = info[info.key == 'attendance']

years = attendance.game_id.str.extract(r'^(?:N|A)LS(\d{4})', expand=False).values
attendance = attendance.assign(year=years)

visual = attendance[['year', 'value']].apply(pd.to_numeric)
visual.columns = ['year', 'attendance']

visual.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=visual.attendance.mean(), label='Mean', linestyle='--', color='green')

plt.show()