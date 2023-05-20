# import csv
# # with open("weather_data.csv") as file:
# #     weather_list_raw = file.readlines()
# #     weather_list = [line.strip() for line in weather_list_raw]
# #     for weather in weather_list:
# #         print(weather)
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print([value for value in temperatures])
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
# #
# # templist = data["temp"].to_list()
# # print(round(sum(templist) / len(templist)))
#
# print(data.temp.max())
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp * 9 / 5 + 32
# print(monday_temp)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
#
# print(data)
# data.to_csv("new_data.csv")

# Primary ..

data = pandas.read_csv("Squirrel_Data.csv")

fur_data = data["Primary Fur Color"].value_counts().reset_index()
fur_data.columns = ["Fur color", "Count"]
print(fur_data)
fur_data.to_csv("squirrel_count.csv")

