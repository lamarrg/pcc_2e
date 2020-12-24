import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # get dates and high temps from this file


    # this part lists the position and value of each portion, to be used below
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # get dates, and high and low temp from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

print(highs)

# plot the high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.75)
ax.plot(dates, lows, c='blue', alpha=0.75)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
plt.title('Daily high and low temperatures, 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
