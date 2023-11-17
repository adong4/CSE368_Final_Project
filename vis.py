import matplotlib as mp
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import pandas as pd


def visual():
    # Load data
    file = './data.xlsx'
    data = pd.read_excel(file)

    # Store data
    city = list(data['city'])
    state = list(data['state'])
    lat = list(data['lat'])
    long = list(data['long'])

    # Visual
    plt.figure(figsize=(80, 48))
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.title('US Cities and Interstates', size=125)
    plt.ylabel('Latitude', size=110)
    plt.xlabel('Longitude', size=110)
    plt.tick_params(axis='y', labelsize=60)
    plt.tick_params(axis='x', labelsize=60)
    plt.grid(True, which='both', lw=2)

    # Plotting
    plt.scatter(long, lat)

    # fig, mapping = plt.subplots()
    # mapping.scatter(long, lat)
    for i, (c, st) in enumerate(zip(city, state)):
        txt = c + ', ' + st
        plt.annotate(txt, (long[i], lat[i]), size=10)
    citystate = [rtn for rtn in zip(city, state)]
    longlat = [rtn for rtn in zip(long, lat)]
    lookuptable = [rtn for rtn in zip(citystate, longlat)]
    citiescon = list(data['connected cities'])
    statecon = list(data['connected cities states'])
    for i, lat1, long1 in enumerate(longlat):
        connected_cities = citiescon[i].split(',')
        connected_states = statecon[i].split(',')
        linesToDraw = zip(connected_cities, connected_states)
        for end in linesToDraw:
            value = lookuptable[end]
            long2 = value[0]
            lat2 = value[1]

            #draw line from long1 lat1 to long2 lat2


    plt.show()


visual()