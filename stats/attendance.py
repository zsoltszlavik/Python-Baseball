import pandas as pd
import matplotlib.pyplot as plt

from data import games

# LO: Pandas selection (row by boolean)
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3']]
attendance.columns = ['year', 'attendance']

# LO: Pandas datatype conversion
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

# LO: Pandas plotting and plot formatting
attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

plt.xlabel('Year')
plt.ylabel('Attendance')

# LO: Pandas aggregate `mean`
plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')

plt.show()
