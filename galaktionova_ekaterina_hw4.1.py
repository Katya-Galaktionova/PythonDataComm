#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program that displays information about
planets.
Create a file using information from the below link -
http://nssdc.gsfc.nasa.gov/planetary/factsheet
Include the mass, diameter, number of
moons and distance from the sun in the file. 
Take this file as an argument. 
Then display results sorted by mass and 
distance from the sun.
"""

import sys
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('planets')

def check_and_get_filename():
    if len(sys.argv) != 2:
        print('Error: must supply 1 argument \nUSAGE: ' + sys.argv[0] + ' filename')
        sys.exit()
    return sys.argv[1]
    
def check_file_exist(file_name_to_check):
    if not os.path.isfile(file_name_to_check):
        print('File ' + file_name_to_check + ' does not exist.')
        sys.exit()

def get_file_data(file_name_to_read):
    try:
        fh = open(file_name_to_read)
        logger.info('File planets has been succefully opened')
        return fh.readlines()
    except:
        logger.info('Could not read file %s' % file_name_to_read, exc_info=True)
    finally:
        fh.close()

def sorted_by_mass(lines):
    planet = {}
    mass = {}
    diameter = {}
    number_of_moons = {}
    dist_from_sun = {}
    for line in lines:
        (planet_name, planet_mass, planet_diameter, planet_no_of_moons, planet_dist_from_sun) = line.split()
        data = {}        
        data['planet'] = planet_name 
        data['mass'] = float(planet_mass) 
        data['diameter'] = float(planet_diameter)
        data['number_of_moons'] = int(planet_no_of_moons)
        data['dist_from_sun']= float(planet_dist_from_sun)
        
        dist_from_sun[data['dist_from_sun']] = data['number_of_moons']
        number_of_moons[data['number_of_moons']] = data['mass']
        mass[data['mass']] = data['diameter']
        diameter[data['diameter']] = data['planet']
        planet[data['planet']] = data['dist_from_sun']  
    
    print('Sorted by mass')
    print('planet'.rjust(12) + 'mass'.rjust(12) + 'diameter'.rjust(12) 
          + 'moons'.rjust(8) + 'dist from sun'.rjust(17))
    print('-'*62)
    for key in sorted(mass.keys()):
        print(diameter[mass[key]].rjust(12) 
        + str(key).rjust(12) + str(mass[key]).rjust(12)
        + str(dist_from_sun[planet[diameter[mass[key]]]]).rjust(8)
        + str(planet[diameter[mass[key]]]).rjust(17)) 
    print('*'*62)
 
def sorted_by_dist_from_sun(lines):
    planet = {}
    mass = {}
    diameter = {}
    number_of_moons = {}
    dist_from_sun = {}
    for line in lines:
        (planet_name, planet_mass, planet_diameter, planet_no_of_moons, planet_dist_from_sun) = line.split()
        data = {}        
        data['planet'] = planet_name 
        data['mass'] = float(planet_mass) 
        data['diameter'] = float(planet_diameter)
        data['number_of_moons'] = int(planet_no_of_moons)
        data['dist_from_sun']= float(planet_dist_from_sun)
        
        dist_from_sun[data['dist_from_sun']] = data['planet']
        planet[data['planet']] = data['mass']
        mass[data['mass']] = data['diameter']
        diameter[data['diameter']] = data['number_of_moons']
        number_of_moons[data['number_of_moons']] = data['dist_from_sun']
    
    print('Sorted by distance from the sun')
    print('planet'.rjust(12) + 'mass'.rjust(12) + 'diameter'.rjust(12) 
          + 'moons'.rjust(8) + 'dist from sun'.rjust(17))
    print('-'*62)
    for key in sorted(dist_from_sun.keys()):
        print(dist_from_sun[key].rjust(12) 
        + str(planet[dist_from_sun[key]]).rjust(12)
        + str(mass[planet[dist_from_sun[key]]]).rjust(12) 
        + str(diameter[mass[planet[dist_from_sun[key]]]]).rjust(8) 
        + str(key).rjust(17))
    
filename = check_and_get_filename()
check_file_exist(filename)
lines = get_file_data(filename)
sorted_by_mass(lines)
sorted_by_dist_from_sun(lines)
