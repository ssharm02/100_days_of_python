import os
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

current_path = os.path.dirname(__file__)
PLACEHOLDER = '[name]'


def read_invited_names():
    new_path = os.path.relpath('.\\Input\\Names\\invited_names.txt', current_path)
    with open(new_path, 'r') as names:
        names_data = names.readlines()
        return names_data


def read_letter():
    new_path = os.path.relpath('.\\Input\\Letters\\starting_letter.txt', current_path)
    with open(new_path, 'r') as letter:
        letter_data = letter.read()
        return letter_data


def write_letter(name, data):
    complete_name = 'Output/ReadyToSend/' + name + ".txt"
    file_one = open(complete_name, 'w')
    file_one.write(data)
    file_one.close()


def main_logic():
    all_names = read_invited_names()
    letter = read_letter()
    for name in all_names:
        stripped_name = name.strip()
        final_message = letter.replace(PLACEHOLDER, stripped_name)
        write_letter(stripped_name, final_message)
        print(final_message)


main_logic()

# name_of_file = input("What is the name of the file: ")
# completeName = '/home/user/Documents'+ name_of_file + ".txt"
# file1 = open(completeName , "w")
# toFile = input("Write what you want into the field")
# file1.write(toFile)
# file1.close()