import dbm

cities = ['Dallas', 'New York', 'Los Angeles']
flights = ['1144', '1020', '2321']

city_flight = dbm.open('cities.dbm', 'n')

for index, flight in enumerate(flights):
	city_flight[flight] = cities[index]

# print(city_flight.items)
city_flight.close()
