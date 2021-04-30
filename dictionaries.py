def test_dictionaries():
    programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                              "Function": "A piece of code that you can easily call over and over again.",
                              "Loop": "The action of doing something over and over"}
    print(programming_dictionary["Bug"])

    # adding to dictionary
    print(programming_dictionary)

    # empty dictionary
    empty_dictionary = {}

    # wipe dictionary
    # programming_dictionary = {}

    programming_dictionary["Bug"] = "Big error in the program"
    print(programming_dictionary)

    # prints out the keys
    for key in programming_dictionary:
        print(key)
        print( programming_dictionary[key])


def exercise():
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }
    # 🚨 Don't change the code above 👆

    # TODO-1: Create an empty dictionary called student_grades.
    student_grades = {}
    # TODO-2: Write your code below to add the grades to student_grades.👇
    for student in student_scores:
        score = student_scores[student]
        if score > 90:
            student_grades[student] = "Outstanding"
        elif score > 80:
            student_grades[student] = "Exceeds Expectations"
        elif score > 70:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"
            # 🚨 Don't change the code below 👇
    print(student_grades)


exercise()


def dictionary_list():
    travel_log = {
        "France": {"cities_visited": ["Paris", "Lille"], "total_number_of_visits": 12},
        "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_number_of_visits": 5}
    }

    # similar to array of object
    travel_log2 = [
        {
            "country": "France",
            "cities_visited": ["Paris", "Lille"],
            "total_number_of_visits": 12
        },
        {
            "country": "Germany",
            "cities_visited": ["Berlin", "Hamburg"],
            "total_number_of_visits": 5
        }
    ]

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited

    travel_log.append(new_country)
    # 🚨 Do NOT change the code above

    # TODO: Write the function that will allow new countries
    # to be added to the travel_log. 👇

    # 🚨 Do not change the code below


# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


