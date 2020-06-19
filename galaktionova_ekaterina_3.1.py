"""
Created on Tue Sep 25 10:51:29 2018

@author: ekaterina

Write a program that takes a filename as an  argument.
If there is no argument, print an error & exit
If the file does not exist print an error & exit
Read the file file1.txt, print the length of the  longest line and the content
(file1.txt is uploaded on canvas).
Extra credit: Implement Argparse as a separate function (5 pts)

"""
import argparse
import os
import sys

def check_and_get_filename():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='file name should be here')
    args = parser.parse_args()
    return args.filename

def check_file_exist(filename_to_check):
    if not os.path.isfile(filename_to_check):
        print('File ' + filename_to_check + ' does not exist.')
        sys.exit()

def get_longest_line(filename_to_analyze):
    fh = open(filename_to_analyze)
    line_length = 0
    line_text = ''
    for line in fh:
        l = len(line)
        if l > line_length:
            line_length = l
            line_text = line
    fh.close()
    return line_text

filename = check_and_get_filename()
check_file_exist(filename)
longest_line = get_longest_line(filename)
print('The longest line in ' + filename + ' is:\n' + longest_line)
