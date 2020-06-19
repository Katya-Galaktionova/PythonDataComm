"""
Add another router to your setup as shown below. 
Enable SSH on it and replicate similar configs as on R1, but with a different IP.

Write a Python script that will SSH into both R1 and R2 and retrieve their running configurations. 
Once you have obtained the running configurations, save it locally in separate files on the VM.
"""

import os
from netmiko import ConnectHandler


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

file1 = 'R1-running-config.txt'
file2 = 'R2-running-config.txt'


ios_r1 = {
    'device_type': 'cisco_ios',
    'username': 'lab',
    'password': 'lab123',
    'ip': '192.168.1.1',
}

ios_r2 = {
    'device_type': 'cisco_ios',
    'username': 'lab',
    'password': 'lab123',
    'ip': '192.168.1.2',
}

net_connect = ConnectHandler(**ios_r1)

print('configurations R1: "show running-config"')
output = net_connect.send_command('show running-config')
response = output.encode()
fh = open(file1, 'wb')
fh.write(response)
fh.close()

net_connect = ConnectHandler(**ios_r2)
print('configurations R2: "show running-config"')
output = net_connect.send_command('show running-config')
response = output.encode()
fh = open(file2, 'wb')
fh.write(response)
fh.close()
