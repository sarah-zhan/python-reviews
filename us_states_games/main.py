# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     # change csv object to a list
#     data = list(csv.reader(file))
#     temperatures = []
#     # loop from the second
#     for row in data[1:]:
#         temperatures.append(int(row[1]))  # change to int
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(data.to_dict())
print(data["temp"].mean())
