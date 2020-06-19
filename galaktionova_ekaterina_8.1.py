
"""
Write a program to ping to 8.8.8.8 and 4.2.2.1.
Ping each IP 50 times.
Use prettytable to print the Avg RTT from the above ping results for
both destinations.
Print the table on the terminal
Additionally, save the output to a file IF the user provides a  filename as 
an argument on the command line.

"""

import subprocess
from prettytable import PrettyTable
import sys


def get_filename():
    if len(sys.argv) == 2:
        return sys.argv[1]
    else:
        return ''

def get_rtt(Ip_address):
    p1 = subprocess.Popen(["ping", "-c", "50", Ip_address], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', '-oE', 'time[=|<](\d*\.\d*)'], stdin=p1.stdout, stdout=subprocess.PIPE)

    data = p2.communicate()
    lines = data[0].decode().split('\n')
    return lines

if __name__ == '__main__':
    filename = get_filename()
    Rtt8888 = get_rtt('8.8.8.8')
    Rtt4221 = get_rtt('4.2.2.1')


table = PrettyTable(["RTT for 8.8.8.8 (ms)", "RTT for 4.2.2.1 (ms)"])        
for i in range(50):
    Rtt8888time = 'timeout'
    Rtt4221time = 'timeout'
    if i < len(Rtt8888):
        Rtt8888time = Rtt8888[i]
    if i < len(Rtt4221):
        Rtt4221time = Rtt4221[i]
    table.add_row([Rtt8888time, Rtt4221time])    
print(table)

if filename != '':
    fh = open(filename, 'w') 
    fh.write(str(table))   
    fh.close()     

