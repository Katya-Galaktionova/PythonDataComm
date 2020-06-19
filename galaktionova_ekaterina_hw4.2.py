"""
Read the previous file in, create dictionaries to
access data by dictionary key.
Check if the file exists, print an error and exit if
not.
Take the file as a variable from the command line.
Take planet as a second variable from the 
command line, if that exists in the file, print its 
record. If it does not exist, print a "not found“
message.
"""

import sys
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('planets')

def check_and_get_arguments():
    if len(sys.argv) != 3:
        print('Error: must supply 2 arguments \nUSAGE: ' + sys.argv[0] + ' filename' + 
              ' planet name: mercury or venus or earth or moon or mars or jupiter or saturn or uranus or netpune or pluto')
        sys.exit()
    return (sys.argv[1], sys.argv[2])

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
        
def get_dictionaries(lines, planet_to_display):        
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
    
        number_of_moons[data['number_of_moons']] = data['planet']
        planet[data['planet']] = data['mass']
        mass[data['mass']] = data['diameter']
        diameter[data['diameter']] = data['dist_from_sun']
        dist_from_sun[data['dist_from_sun']] = data['number_of_moons']
    print('planet'.rjust(12) + 'mass'.rjust(12) + 'diameter'.rjust(12) 
          + 'moons'.rjust(8) + 'dist from sun'.rjust(17))
    print('-'*62)
    if planet_to_display in planet.keys():
        print(planet_to_display.rjust(12) + str(planet[planet_to_display]).rjust(12)
        + str(mass[planet[planet_to_display]]).rjust(12)
        + str(dist_from_sun[diameter[mass[planet[planet_to_display]]]]).rjust(8) 
        + str(diameter[mass[planet[planet_to_display]]]).rjust(17))
 
(file_name, planet_name) = check_and_get_arguments()
check_file_exist(file_name)
lines = get_file_data(file_name)
get_dictionaries(lines, planet_name)

