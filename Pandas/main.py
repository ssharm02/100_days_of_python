
def read_csv_file():
    with open("weather_data.csv") as data_file:
        data = data_file.readlines()
        print(data)


def read_with_csv():
    import csv
    with open("weather_data.csv") as data_file:
        data = csv.reader(data_file)
        temperatures = []
        for row in data:
            if row[1] != "temp":
                temperatures.append(int(row[1]))
        print(temperatures)


def read_with_pandas():
    import pandas
    data = pandas.read_csv("weather_data.csv")
    temperature = data["temp"].to_list()
    data_dict = data.to_dict()
    average_temp = sum(temperature) / len(temperature)
    print(data["temp"].mean())
    print(data["temp"].max())
    print(data["condition"])
    # print(data.condition)
    print(average_temp)
    print(data_dict)
    print(temperature)
    # selecting a panda data row
    print(data[data.day == "Monday"])
    # show row with highest temperature
    print(data[data.temp == data["temp"].max()])
    monday = data[data.day == "Monday"]
    print("monday is ", monday)
    monday_temp = int(monday.temp)
    monday_temp_f = monday_temp * 9/5 + 32
    print(monday_temp_f)
    # create a panda data frame from scratch
    data_dict = {
        "students": ["Sarthak", "Buddy", "Neelu"],
        "Scores": [99, 77, 88]
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("new_data.csv")


read_with_pandas()