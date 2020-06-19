
"""
Create a states database.
Print an error if the file is not there.
Allow the user to specify a two letter state  abbreviation on the command line.
Use functions to query the db.
Print the response
Note: Upload the db files with your code.
"""

import sqlite3
from sqlite3 import Error
import sys
import os
#from prettytable import PrettyTable

def check_and_get_filename():
    if len(sys.argv) == 1:
        print('File name is not specified. Please provide a file name.')
        sys.exit()
    return sys.argv[1]

def check_file_exist(filename_to_check):
    if not os.path.isfile(filename_to_check):
        print('File ' + filename_to_check + ' does not exist.')
        sys.exit()

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def prompt_user():
     return str(input('''Please type two letters abbreviation of the state: ''')).upper()
 
def get_reader(conn, choice):
    sqlcommand = '''select stateName, abbreviation from state
                           where abbreviation = ? '''
    t = (choice,)
    try:
        c = conn.cursor()
        c.execute(sqlcommand, t)
        print(c.fetchall())
    except Error as e:
        print(e)
    finally:
        c.close()

def main():
    database = 'states.db'
    conn = create_connection(database)
    
    if conn is not None:
        user_choice = prompt_user()
        get_reader(conn, user_choice)
        conn.close()
    else:
        print('Error! cannot create database connection!')
              
if __name__ == '__main__':
    main()