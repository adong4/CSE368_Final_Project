from env1 import generate


def bfs(start_city, end_city):
    counter = 0
    queue = []
    visited = []
    route = []
    previous_cities = []

    queue.append(start_city)

    while queue:
        current_city = queue.pop(0)
        visited.append(current_city)
        counter += 1

        if current_city == end_city:
            route.append(end_city)
            # route creating
            city = end_city
            for i in range(counter):  # amount of times loopings needed to be done (not too sure if needed)
                for cities in previous_cities:  # loops through list of city to check
                    if city == cities[0]:  # matches the city to find the previous city
                        route.append(cities[1])  # adds previous city to the route
                        city = cities[1]  # updates the city to backtrack
            route.reverse()
            print(route)
            print(counter)
            return route

        for connected_cities in G.edges(current_city):
            if connected_cities[1] not in visited:
                queue.append(connected_cities[1])
                previous_cities.append([connected_cities[1], current_city])  # to help backtrack later on