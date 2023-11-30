import matplotlib.pyplot as plt
import pandas as pd


def visual(search, route):
    # Load data
    file = './data.xlsx'
    data = pd.read_excel(file)+

    # Store data
    city = list(data['city'])
    state = list(data['state'])
    lat = list(data['lat'])
    long = list(data['long'])

    # Visual
    plt.figure(figsize=(80, 48))
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.title(search + ' on US Cities and Interstates', size=125)
    plt.ylabel('Latitude', size=110)
    plt.xlabel('Longitude', size=110)
    plt.tick_params(axis='y', labelsize=60)
    plt.tick_params(axis='x', labelsize=60)
    plt.grid(True, which='both', lw=2)

    # Plotting
    plt.scatter(long, lat, lw=10)
    # fig, mapping = plt.subplots()
    # mapping.scatter(long, lat)
    for i, (c, st) in enumerate(zip(city, state)):
        txt = c + ', ' + st
        plt.annotate(txt, (long[i], lat[i]), size=10)

    # New data load
    citystate = [rtn for rtn in zip(city, state)]
    longlat = [rtn for rtn in zip(long, lat)]
    lookuptable = dict([rtn for rtn in zip(citystate, longlat)])
    citiescon = list(data['connected cities'])
    statecon = list(data['connected cities states'])
    for i, (long1, lat1) in enumerate(longlat):
        connected_cities = citiescon[i].split(', ')
        connected_states = statecon[i].split(', ')
        linesToDraw = zip(connected_cities, connected_states)
        for value in linesToDraw:
            longlat2 = lookuptable[value]
            long2 = longlat2[0]
            lat2 = longlat2[1]

            # draw line from long1 lat1 to long2 lat2
            plt.plot(list([long1, long2]), list([lat1, lat2]), lw=4, color='r')

    # now plot path
    coordinatesPath = list()
    for value in route:
        pathcity, pathstate = value.split(', ')
        coordinatesPath.append(lookuptable[pathcity, pathstate])
    i = 0
    while i < len(coordinatesPath)-1:
        longlat1 = coordinatesPath[i]
        long1 = longlat1[0]
        lat1 = longlat1[1]
        longlat2 = coordinatesPath[i + 1]
        long2 = longlat2[0]
        lat2 = longlat2[1]
        plt.plot(list([long1, long2]), list([lat1, lat2]), linestyle='dotted', lw=8, color='yellow')
        i += 1

    plt.show()
