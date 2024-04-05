import pandas

# data = pandas.read_csv("weather_data.csv")
# temp = data["temp"].mean()
#
# max_temp = data["temp"].max()
#
# print(data.condition)
#
# print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp = monday.temp[0]
# print(monday_temp)

# Create dataframe
# data_dict = {
#    "student": ["Amy", "James", "Angela"],
#    "score": [75, 53, 78]
#
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")



data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240405.csv")

gray_fur = data["Primary Fur Color"]

cinnamon_fur = data["Primary Fur Color"]

black_fur = data["Primary Fur Color"]


# Create dataframe
fur_dict = {
  "Fur Color": ["gray", "red", "black"],
  "Count": [gray_fur[gray_fur == "Gray"].count(), cinnamon_fur[cinnamon_fur == "Cinnamon"].count(), black_fur[black_fur == "Black"].count()]

}

fur_data = pandas.DataFrame(fur_dict)
fur_data.to_csv("fur_data.csv")