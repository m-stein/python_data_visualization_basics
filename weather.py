import csv
import matplotlib.pyplot as plt

from datetime import datetime


def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8


def plot_data_from_file(ax_temp, ax_rain, path, color):
    dates, rainfalls, highs, lows = [], [], [], []
    name = ''
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)

        # Read all data from the csv file into lists.
        # Note that this can be done only once on the reader object!
        for dict in reader:
            name = dict['NAME']
            date = datetime.strptime(dict["DATE"], '%Y-%m-%d')
            try:
                # It is important to convert to float or int here as otherwise,
                # the values stay strings and pyplot will mix up the y-axis ticks!
                high = float(dict["TMAX"])
                low = float(dict["TMIN"])
                rainfall = float(dict["PRCP"])
            except ValueError:
                print(f'Warning: data for date {date} in file {path} incomplete, skipping')
            else:
                dates.append(date)
                highs.append(fahrenheit_to_celsius(high))
                lows.append(fahrenheit_to_celsius(low))
                rainfalls.append(rainfall)

    ax_temp.plot(dates, highs, color=color, linewidth=1, alpha=0.3)
    ax_temp.plot(dates, lows, color=color, linewidth=1, alpha=0.3)
    ax_rain.bar(dates, rainfalls, color=color, linewidth=1, alpha=0.3, width=1, label=name)
    ax_temp.fill_between(dates, highs, lows, facecolor=color, alpha=0.3, label=name)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(1,2)
plot_data_from_file(ax[0], ax[1], 'weather_sitka_2021_simple.csv', 'blue')
plot_data_from_file(ax[0], ax[1], 'weather_death_valley_2021_simple.csv', 'red')
ax[0].set_title(f'Daily Temperatures', fontsize=16)
ax[0].set_ylabel("Temperature (°C)", fontsize=12)
ax[0].set_xlabel("")
ax[0].legend(loc='best')
ax[1].set_title(f'Daily Rainfall', fontsize=16)
ax[1].set_ylabel("PRCP", fontsize=12)
ax[1].set_xlabel("")
ax[1].legend(loc='best')

# Let pyplot print the x-axis ticks more pretty considering that they are dates.
fig.autofmt_xdate()

plt.show()
