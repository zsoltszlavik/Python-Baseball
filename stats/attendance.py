import pandas as pd
import matplotlib.pyplot as plt

from data import games

info = games.loc[games['type'] == 'info']

attendance = info.loc[info['multi2'] == 'attendance']

attendance = attendance.loc[:, ['year', 'multi3']].apply(pd.to_numeric)
attendance.columns = ['year', 'attendance']

attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')

plt.show()
