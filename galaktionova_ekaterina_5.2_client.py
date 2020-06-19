
"""
Create a python client and server. Save client.py and server.py in different directories on your system
    Eg: workspace1 directory has client.py and workspace2   
          directory has server.py

Client:
Take the IP address, port as command line arguments on client.
When you run client code you should be prompted to enter a command in the following format:
	get <filename>, 
    where filename is name of a text file like file1.txt, file2.txt etc
Server: (Create and store your choice of any .txt files in the same directory your server.py exists)
Take the IP address and port as arguments to the server.
Listen for any messages from client.
Once you get the message in format get <filename>, extract the filename and check if file exists in the directory server.py is in.
If it exists, transfer file from server to client. After the code runs, a copy of the file should have appeared in the directory client.py is stored in.
If filename does not exist in server’s directory send a message from server to client saying “Sorry file not found”. This message must be printed on client terminal.

Went for Extra-credit
Implement Homework 5.2 to work for any type of file i.e.
      any extension like .jpg, .png, .mp3, .pdf etc and not limited to  
      .txt.

"""

import socket
import sys

def check_and_get_arguments():
    if len(sys.argv) != 3:
        print('Error: must supply 2 arguments \nUSAGE: ' + sys.argv[0] + ' IP address' + ' port number')
        sys.exit()
    return (sys.argv[1], int(sys.argv[2]))

def create_client_socket():
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    return client_socket

def waiting_message(IP_address, port, client_socket):
    while True:
        message = input('Please provide command to send to server: ')
        split = message.split()
        command = split[0].upper()
        client_socket.sendto(message.encode(),(IP_address,port))        
        if command == 'EXIT':
            break
        if command == 'GET':
            filename = split[1]
            read_file(client_socket, filename)
            
def read_file(client_socket, filename):
    print ('Receiving file')
    fh = open(filename, 'wb')
    while True:
        (read_data,server_address) = client_socket.recvfrom(2048)
        if not read_data:
            break
        fh.write(read_data)
    fh.close()
    (read_data,server_address) = client_socket.recvfrom(2048)
    print(read_data.decode())
            
        
if __name__=='__main__':
    (IP_address, port) = check_and_get_arguments()
    client_socket = create_client_socket()
    waiting_message(IP_address, port, client_socket)
    client_socket.close()


