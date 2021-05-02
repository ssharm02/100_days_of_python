# list comprehension demo

def playing_with_original_list():
    numbers = [1, 2, 3]
    new_list = []
    for n in numbers:
        add_1 = n + 1
        new_list.append(add_1)
    print(new_list)


# Removes a lot of lines of code makes it more readable
def list_comprehension():
    numbers = [1, 2, 3]
    name = "Sarthak"
    names = ["Sarthak", "Buddy", "Sakshi", "Bal", "Neelu", "Dofus"]
    new_list = [number + 1
                for number in numbers]
    print(new_list)
    letters_list = [letter
                    for letter in name]
    print(letters_list)
    ranged_list = [num * 2
                   for num in range(1, 5)]
    print(ranged_list)
    # conditional list comprehension
    legit_names = [name.upper()
                   for name in names if len(name) > 5]
    print(legit_names)


def list_comprehension_challenge():
    original_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [num * num
                       for num in original_numbers]
    print(squared_numbers)
    numbers_2 = [num
                 for num in numbers if num % 2 == 0]
    print(numbers_2)


def list_comprehension_challenge_2():
    file_1 = open("file1.txt", 'r').readlines()
    file_2 = open("file2.txt", 'r').readlines()
    common_numbers = [int(num)
                      for num in file_1 if num in file_2]
    print(common_numbers)


list_comprehension_challenge_2()