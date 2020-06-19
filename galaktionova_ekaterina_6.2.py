#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Query the planets database.
Print an error if the file is not there.
Let the user pass in from the command line:
1: Display by distance from sun
2: Display alphabetically
3: Display by mass.
Print using prettytables.
Note: Submit the db files along with your code

Note: Database creates along this file execution. No external file is needed.
"""

import sqlite3
from sqlite3 import Error
from prettytable import PrettyTable


## create database

rows = [('mercury', 0.330, 4879, 0, 57.9),
        ('venus', 4.87, 12104, 0, 108.2),
        ('earth', 5.97, 12756, 1, 149.6),
        ('moon', 0.073, 3475, 0, 0.384),
        ('mars', 0.642, 6792, 2, 227.9),
        ('jupiter', 1898, 142984, 79, 778.6),
        ('saturn', 568, 120536, 62, 1433.5),
        ('uranus', 86.8, 51118, 27, 2872.5),
        ('netpune', 102, 49528, 14, 4495.1),
        ('pluto', 0.0146, 2370, 5, 5906.4)] 

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def check_table_exists(conn, table_name):
    c = conn.cursor()
    try:
        c.execute('''select name from sqlite_master where type = 'table' and name = '{0}' '''
                           .format(table_name))
        tables = c.fetchall();
        return tables is not None and len(tables) == 1
    except Error as e:
        print(e)
        return False
    finally:
        c.close()
           
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        c.close()

def fill_table(conn, rows):
    try:
        c = conn.cursor()
        c.executemany('insert into planets values (?,?,?,?,?)', rows)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        c.close()
 
def prompt_user():
     return int(input('''If you want to see planets sorted by distance from the sun, print 1,
                    if you want to see planets sorted by name, print 2,
                    if you want to see planets sorted by mass, print 3: '''))

def get_reader(conn, choice):
    sqlcommand = ''
    if choice == 1:
        sqlcommand = '''select * from planets
                           order by distance_from_the_sun'''
    elif choice ==2:
        sqlcommand ='''select * from planets
                           order by name'''
    elif choice ==3:
        sqlcommand ='''select * from planets
                           order by mass'''
    try:
        c = conn.cursor()
        c.execute(sqlcommand)
        return c.fetchall()
    except Error as e:
        print(e)
    finally:
        c.close()
        
def print_table(data):
    if data is not None:
        table = PrettyTable(["Planet", "Mass", "Diameter", "Number of moons", "Distance from the sun"])        
        for row in data:
            table.add_row([row[0], row[1], row[2], row[3], row[4]])    
        print(table) 
    else:
        print('Error! There is no table to display!')

    
def main():
    database = 'planets.db'
    sql_create_planets_table = '''CREATE TABLE planets (name varchar(25), mass float, 
    diameter float, number_of_moons int, distance_from_the_sun float)'''
    conn = create_connection(database)
    if conn is not None:
        if check_table_exists(conn, 'planets') == False:
            create_table(conn, sql_create_planets_table)
            fill_table(conn, rows)

        user_choice = prompt_user()
        reader = get_reader(conn, user_choice)
        print_table(reader)
        conn.close()
    else:
        print('Error! cannot create database connection!')
                    
              
if __name__ == '__main__':
    main()

