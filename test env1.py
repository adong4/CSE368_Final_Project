import pandas as pd
import networkx as nx
import random
from queue import PriorityQueue
from env1 import generate
from vis import visual


def bfs(start_city, end_city):
    counter = 0
    queue = []
    visited = []
    route = []
    previous_cities = []

    queue.append(start_city)

    start_time = time.time()
    
    while queue:
        current_city = queue.pop(0)
        visited.append(current_city)
        counter += 1

        if current_city == end_city:
            end_time = time.time() - start_time
            print("Time it took: ", end_time)
            route.append(end_city)
            
            # route creating
            city = end_city
            for i in range(counter):  # amount of times loopings needed to be done (not too sure if needed)
                for cities in previous_cities:  # loops through list of city to check
                    if city == cities[0]:  # matches the city to find the previous city
                        route.append(cities[1])  # adds previous city to the route
                        city = cities[1]  # updates the city to backtrack
            # route.reverse()
            # print(route)
            # print(counter)
            return route, counter

        for connected_cities in G.edges(current_city):
            if connected_cities[1] not in visited:
                queue.append(connected_cities[1])
                previous_cities.append([connected_cities[1], current_city])  # to help backtrack later on


def A_star(start_city, end_city):
    priority_queue = PriorityQueue()
    visited = set()
    route = []
    previous_cities = []
    counter = 0
    start_node_tuple = (0, start_city)

    start_time = time.time()
    
    list_of_connected_cities_and_distance = []
    for edge in G.edges.data():
        list_of_connected_cities_and_distance.append(list([edge[0], edge[1], int(edge[2]['distance'])]))

    priority_queue.put(start_node_tuple)

    while priority_queue:
        counter += 1
        tup = priority_queue.get()
        distance, parent_city = tup[0], tup[1]
        visited.add(parent_city)
        if parent_city == end_city:
            end_time = time.time() - start_time
            print("Time it took: ", end_time)
            route.append(end_city)

            # route creating
            city = end_city
            for i in range(counter):  # amount of times loopings needed to be done (not too sure if needed)
                for the_cities in previous_cities:  # loops through list of city to check
                    if city == the_cities[1]:  # matches the city to find the previous city
                        route.append(the_cities[0])  # adds previous city to the route
                        city = the_cities[0]  # updates the city to backtrack
            # route.reverse()
            # print(route)
            # print(distance)
            # print(counter)
            return route, distance, counter

        cities = []
        for connected_cities in G.edges(parent_city):
            for find_distance in list_of_connected_cities_and_distance:
                if connected_cities[0] in find_distance and connected_cities[1] in find_distance:
                    distance_of_connected_cities = find_distance[2]
            if connected_cities[1] not in visited:
                tuple_placeholder = (distance_of_connected_cities + distance, connected_cities[1])
                cities.append(tuple_placeholder)
                child_tup = tuple_placeholder
                priority_queue.put(child_tup)
                newcity, newdistance = child_tup[1], child_tup[0]
                previous_cities.append((parent_city, newcity))


def random_two_cities(twocities):
    random_cities = random.choice(twocities)
    random_first_city = random_cities
    random_cities = random.choice(twocities)
    random_second_city = random_cities
    while random_first_city == random_second_city:
        random_cities = random.choice(twocities)
        random_second_city = random_cities
    random_first_city = str(random_first_city[0]) + ', ' + str(random_first_city[1])
    random_second_city = str(random_second_city[0]) + ', ' + str(random_second_city[1])
    return random_first_city, random_second_city


file = './data.xlsx'
data = pd.read_excel(file)
G = nx.Graph()
generate(data, G)

randCity = list(data['city'])
randState = list(data['state'])
randCityState = [rtn for rtn in zip(randCity, randState)]
RandCity1, RandCity2 = random_two_cities(randCityState)
print(RandCity1, RandCity2)


# BFS
pathBFS, countBFS = bfs(RandCity1, RandCity2)
visual('BFS', pathBFS)
print("Node Count for BFS: ", countBFS)

# A^star
pathAstar, distanceAstar, countAstar = A_star(RandCity1, RandCity2)
visual('A_star', pathAstar)
print("Node Count for A*: ", countAstar, " || Distance: ", distanceAstar, " meters")

# bfs('Anniston, AL', 'Auburn-Opelika, AL')
# path, count = bfs('Santa Clarita, CA', 'Charleston, WV')
# path, distance, count = A_star('Santa Clarita, CA', 'Charleston, WV')
# visual('A_star', path)
