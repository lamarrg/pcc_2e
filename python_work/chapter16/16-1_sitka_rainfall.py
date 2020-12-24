# Sitka is in a temperate rainforest, so it gets a fair amount of rainfall. In the data file sitka_weather_2018_simple.csv is a header called PRCP, which represents daily rainfall amounts. Make a visualization focusing on the data in this column. You can repeat the exercise for Death Valley if you’re curi- ous how little rainfall occurs in a desert.

import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# print(header_row)

    dates, precip = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        dates.append(current_date)
        precip.append(rain)


# plot the high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precip, c='blue')

# format plot
plt.title('Daily precipitation, Siska 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (inches)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
