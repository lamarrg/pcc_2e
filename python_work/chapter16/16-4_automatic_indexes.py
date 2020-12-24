# n this section, we hardcoded the indexes correspond- ing to the TMIN and TMAX columns. Use the header row to determine the indexes for these values, so your program can work for Sitka or Death Valley. Use the station name to automatically generate an appropriate title for your graph as well.

# created function to work with any file that has the required columns

import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename1 = 'data/death_valley_2018_simple.csv'
filename2 = 'data/sitka_weather_2018_simple.csv'


def create_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        city_name = ''
        for index, column_header in enumerate(header_row):
            print(f'death valley - {index}, {column_header}')

            if column_header == 'TMIN':
                low_index = index
            if column_header == 'TMAX':
                high_index = index
            if column_header == 'NAME':
                city_index = index

        # Get dates, and high and low temperatures from this file.
        dates, highs, lows = [], [], []

        for row in reader:
            if city_name == '':
                city_name = row[city_index]
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f'Missing data for death valley - {current_date}')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


    # plot the high and low temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.75)
    ax.plot(dates, lows, c='blue', alpha=0.75)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


    # format plot
    title = f'Daily high and low temperatures, 2018\n{city_name}'
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


create_data(filename1)
