"""
Write a program that reads data from file2 and creates a list of lists (no sort order needed,
follow order in file).

The final list should be printed and should look like this:

     [[voldemort,cat],[harry,owl],[hermoine,toad],…so on…..]]

Handle all possible errors for full extra credit.

     (Hint: Think about what errors you may face when trying to
       read a file!)

"""

import sys
import os

def check_and_get_filename():
    if len(sys.argv) == 1:
        print('File name is not specified. Please provide a file name.')
        sys.exit()
    return sys.argv[1]

def check_file_exist(filename_to_check):
    if not os.path.isfile(filename_to_check):
        print('File ' + filename_to_check + ' does not exist.')
        sys.exit()

def get_lists(filename_to_analyze):
    fh = open(filename_to_analyze)
    person_names = []
    pet_names = []
    for line in fh:
        words = line.split()
        if len(words) == 0:
            continue
        if len(person_names) < 9:
            person_names.extend(words)
        else:
            pet_names.extend(words)
    fh.close()
    return (person_names, pet_names)

def get_list_of_lists(person_names_1, pet_names_1):
    list_of_lists = []
    for i in range(len(person_names_1)):
        list_of_lists.append([person_names_1[i], pet_names_1[i]])
    print(list_of_lists)

filename = check_and_get_filename()
check_file_exist(filename)
(person_names, pet_names) = get_lists(filename)
get_list_of_lists(person_names, pet_names)
