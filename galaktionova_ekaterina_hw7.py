
"""
HW7
"""

from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

#import logging

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1') 
def page1():
    planets = get_table()
    return render_template('page1.html', planets = planets)

def get_table():       
    conn = sqlite3.connect('planets.db')
    
    if conn is not None:
        sqlcommand = '''select * from planets'''
        try:
            c = conn.cursor()
            c.execute(sqlcommand)
            return c.fetchall()
        except Error as e:
            return []
        finally:
            c.close()
            conn.close()
    else:
        return []
    
@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3', methods=['POST'])
def page3():
    choice = request.form['choice']
    planet = get_planet(choice)
    return render_template('page3.html', planets = planet)
    
def get_planet(choice):       
    conn = sqlite3.connect('planets.db')

    if conn is not None:
        sqlcommand = '''select * from planets where name = ? '''
        t = (choice, )
        try:
            c = conn.cursor()
            c.execute(sqlcommand, t)
            return c.fetchall()
        except Error as e:
            return []
        finally:
            c.close()
            conn.close()
    else:
        return []

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)