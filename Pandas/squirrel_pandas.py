import pandas


def read_with_pandas():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
    red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
    print(grey_squirrels)
    print(red_squirrels)
    print(black_squirrels)
    data_dict = {
        "Fur Color": ["Gray", "Cinnamon", "black"],
        "Count": [grey_squirrels, red_squirrels, black_squirrels]
    }
    df = pandas.DataFrame(data_dict)
    df.to_csv("squirrel.csv")

read_with_pandas()