

import sys
import socket

def create_socket(server_port):

##Define socket
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
##Server socket should bind to one IP and port it is listening on. This must match with dest port on client
    server_socket.bind(('127.0.0.1',server_port))
    print("Server is ready to receive ")

##Always listening
    while True:
        command,client_address=server_socket.recvfrom(2048)
        print("The message client sent is:")
        print(command.decode())

        print("\nWe are now responding back...")
#Interpret command and give response
        response="I hear you and I agree!"
        server_socket.sendto(response.encode(),client_address)
        print("Done")

if __name__=="__main__":
    server_port=5555
    create_socket(server_port)


