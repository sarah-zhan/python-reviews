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

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(data.to_dict())
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"].temp * 9/5 + 32)

# create dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors_count = data.groupby("Primary Fur Color")["Primary Fur Color"].count()
colors_count.to_csv("squirrel_count.csv", header=["Count"])






