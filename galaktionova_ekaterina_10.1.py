"""
Write a Python script that will SSH into R1 and print the following details:

	- The routing table on R1
	- The arp table on R1
	- A brief status of all interfaces on R1
"""


from netmiko import ConnectHandler


ios_r1 = {
    'device_type': 'cisco_ios',
    'username': 'lab',
    'password': 'lab123',
    'ip': '192.168.1.1',
}

net_connect = ConnectHandler(**ios_r1)

print('Routing table on R1: "show ip route"')
output1 = net_connect.send_command('show ip route')
print(output1)

print('Arp table on R1: "show arp"')
output2 = net_connect.send_command('show arp')
print(output2)

print('Status of all interfaces on R1: "sh ip int br"')
output3 = net_connect.send_command('sh ip int br')
print(output3)

quit()
