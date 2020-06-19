"""
Write a program that takes an argument of file2.txt and
a sort order
Read the words from file2 into a list.
Sort the list based on the order specified by the user and print a table
as output. Below is an example:
Below is forward sorting (alphabetical):
person name	pet name
Albert		Armadillo
Bob			Baboon
"""

import sys
import os

def check_and_get_arguments():
    if len(sys.argv) != 3:
        print('Error: must supply 2 arguments \nUSAGE: ' + sys.argv[0] + ' filename' + ' order to sort: MUST chose asc or desc')
        sys.exit()
    to_sort_asc = True
    if sys.argv[2] == 'desc':
        to_sort_asc = False
    return (sys.argv[1], to_sort_asc)

def check_file_exist(file_name_to_check):
    if not os.path.isfile(file_name_to_check):
        print('File ' + file_name_to_check + ' does not exist.')
        sys.exit()

def get_lists(file_name_to_analyze):
    fh = open(file_name_to_analyze)
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

def sort_list(names, to_sort_asc):
    names.sort()
    if to_sort_asc == False:
        names.reverse()

def print_names(list1, list2):
    print('person name'.rjust(12) + 'pet name'.rjust(12))
    print('-'*30)
    for i in range(len(list1)):
        print(list1[i].rjust(12) + list2[i].rjust(12))    

(file_name, to_sort_asc) = check_and_get_arguments()
check_file_exist(file_name)
(person_names, pet_names) = get_lists(file_name)
sort_list(person_names, to_sort_asc)
sort_list(pet_names, to_sort_asc)
print_names(person_names, pet_names)

os.getcwd()

fh = open('planets.txt')
for line in fh:
    print(line)

fh = open('planets.txt')    
my_list =[]
for line in fh:
    my_list.append(line)
fh.close()
print(my_list)

