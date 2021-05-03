import random
import pandas
# how to use dictionary comprehension


def dictionary_comprehension_test():
    names = ["Sarthak", "Buddy", "Sakshi", "Bal", "Neelu", "Dofus"]
    students_score = {student: random.randint(1, 101) for student in names}
    print(students_score)


def dictionary_comprehension_if_condition():
    full_dict = {'Sarthak': 39, 'Buddy': 52, 'Sakshi': 22, 'Bal': 9, 'Neelu': 23, 'Dofus': 77}
    passed_students = {student: score
                       for (student, score) in full_dict.items() if score > 60}
    print(passed_students)


def dictionary_comprehension_count_letters():
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    count_words = {word: len(word)
                   for word in sentence.split()}
    print(count_words)


def dictionary_temp_conversion():
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    converted_temps = {day: (temp * 9/5) + 32
                       for (day, temp) in weather_c.items()}
    print(converted_temps)


def pandas_dictionary_comprehension():
    student_dict = {
        "student": ["Sarthak", "Buddy", "Sakshi", "Bal", "Neelu", "Dofus"],
        "score": [99, 93, 64, 77, 98, 0]
    }
    student_data_frame = pandas.DataFrame(student_dict)
    # print(student_data_frame)

    # Loop through a data frame
    # for (key, value) in student_data_frame.items():
    #     print(key, value)
    # better pandas loop iter rows
    for (index, row) in student_data_frame.iterrows():
        # print(row.student)
        # print(row.score)
        if row.student == "Sarthak":
            print(row.score)


pandas_dictionary_comprehension()
