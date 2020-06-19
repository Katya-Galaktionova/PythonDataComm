
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
import os
import sys

def check_and_get_arguments():
    if len(sys.argv) != 3:
        print('Error: must supply 2 arguments \nUSAGE: ' + sys.argv[0] + ' IP address' + ' port number')
        sys.exit()
    return (sys.argv[1], int(sys.argv[2]))

def create_server_socket(IP_address, port):
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((IP_address, port))
    print("Server is ready to receive ")
    return server_socket

def waiting_message(server_socket):
    while True:
        (message, client_address) = server_socket.recvfrom(2048)
        # message = 'Get filename.txt'
        command = message.decode().split()
        result = process_message(command, server_socket, client_address)
        if result == True:
            break
        
def process_message(message, server_socket, client_address):     
    command = message[0].upper()
    print(command)
    if command == 'EXIT':
        return True
    if command == 'GET':
        filename = message[1]
        print(filename)
        if check_file_exist(filename) == True:
            print('Sending file')
            read_data = get_filedata(filename)
            try:
                for data in read_data:
                    server_socket.sendto(data, client_address)
                print('File sent')
            except:
                print('Error to send file')
            # Client expects empty message to finish file download.
            server_socket.sendto(''.encode(), client_address)
            server_socket.sendto('Finished'.encode(), client_address)
        else:
            server_socket.sendto(''.encode(), client_address)
            server_socket.sendto('Sorry file not found'.encode(), client_address)
    return False
    
def check_file_exist(file_name_to_check):
    if not os.path.isfile(file_name_to_check):
        print('File ' + file_name_to_check + ' does not exist.')
        return False
    return True
        
def get_filedata(filename):
    filedata = []
    fh = open(filename, 'rb')
    while True:
        data = fh.read(2048)
        if not data:
            break
        filedata.append(data)
    fh.close()
    return filedata

if __name__=='__main__':
    (IP_address, port) = check_and_get_arguments()
    server_socket = create_server_socket(IP_address, port)
    waiting_message(server_socket)
    server_socket.close()






