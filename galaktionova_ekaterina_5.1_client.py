"""
Create a python client and server.
Take the IP address, port as command line arguments on client.
When you run client code you should be prompted to enter a message.
Take the IP address and port as arguments to the server.
After the message has been received on the server, send back reply as acknowledgement or proof that communication occurred.

"""

import socket
import sys

def check_and_get_arguments():
    if len(sys.argv) != 3:
        print('Error: must supply 2 arguments \nUSAGE: ' + sys.argv[0] + ' IP address' + ' port number')
        sys.exit()
    return (sys.argv[1], int(sys.argv[2]))

def create_client_socket(message, IP_address, port):
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    
        client_socket.sendto(message.encode(),(IP_address,port))
        print("Message sent. Waiting for reply.")
        response,server_address=client_socket.recvfrom(2048)
        print("Got reply back from server! Server reply is:")
        print(response.decode())
        client_socket.close()

if __name__=='__main__':
    (IP_address, port) = check_and_get_arguments()
    message=input("Please enter a message:\n")
    create_client_socket(message, IP_address, port)

     