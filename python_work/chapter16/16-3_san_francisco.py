# Are temperatures in San Francisco more like tempera- tures in Sitka or temperatures in Death Valley? Download some data for San Francisco, and generate a high-low temperature plot for San Francisco to make a comparison.


import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
filename2 = 'data/sitka_weather_2018_simple.csv'
filename3 = 'data/san_fran_2018.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(f'death valley - {index}, {column_header}')

    # Get dates, and high and low temperatures from this file.
    dv_dates, dv_highs, dv_lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for death valley - {current_date}')
        else:
            dv_dates.append(current_date)
            dv_highs.append(high)
            dv_lows.append(low)


with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(f'sitka - {index}, {column_header}')

    # Get dates, and high and low temperatures from this file.
    s_dates, s_highs, s_lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f'Missing data for Sitka - {current_date}')
        else:
            s_dates.append(current_date)
            s_highs.append(high)
            s_lows.append(low)


with open(filename3) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(f'san fran - {index}, {column_header}')

    # Get dates, and high and low temperatures from this file.
    sf_dates, sf_highs, sf_lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for San Fran - {current_date}')
        else:
            sf_dates.append(current_date)
            sf_highs.append(high)
            sf_lows.append(low)



# plot the high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dv_dates, dv_highs, c='red', alpha=0.75)
ax.plot(dv_dates, dv_lows, c='blue', alpha=0.75)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.1)

ax.plot(s_dates, s_highs, c='green', alpha=0.75)
ax.plot(s_dates, s_lows, c='orange', alpha=0.75)
plt.fill_between(s_dates, s_highs, s_lows, facecolor='green', alpha=0.1)

ax.plot(sf_dates, sf_highs, c='purple', alpha=0.75)
ax.plot(sf_dates, sf_lows, c='yellow', alpha=0.75)
plt.fill_between(sf_dates, sf_highs, sf_lows, facecolor='purple', alpha=0.1)

# format plot
title = 'Daily high and low temperatures, 2018\nDeath Valley / Sitka / San Fran'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

