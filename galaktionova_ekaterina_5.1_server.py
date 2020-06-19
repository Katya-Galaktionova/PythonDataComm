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

def create_server_socket(IP_address, port):

    server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((IP_address, port))
    print("Server is ready to receive ")

    while True:
        command,client_address=server_socket.recvfrom(2048)
        print("The message client sent is:")
        print(command.decode())

        print("\nWe are now responding back...")
        response="I hear you and I agree!"
        server_socket.sendto(response.encode(),client_address)
        print("Done")
        break
    server_socket.close()

if __name__=='__main__':
    (IP_address, port) = check_and_get_arguments()
    create_server_socket(IP_address, port)
            