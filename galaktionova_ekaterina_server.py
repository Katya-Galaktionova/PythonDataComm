import sys
import os
import socket
import threading

def check_and_get_arguments():
    if len(sys.argv) != 3:
        print('Error: must supply 2 arguments \nUSAGE: ' + sys.argv[0] + ' /folder' + ' port number')
        sys.exit()
    return (sys.argv[1], int(sys.argv[2]))

def create_server_socket(port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', port))
    serversocket.listen(5)
    return serversocket

def check_create_server_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.makedirs('server\\' + folder_name)

def read_passwords(config_file_path):
    return []

def handle_client_connection(connection, passwords):
    print('Created thread for client')
    connection.close()

if __name__=='__main__':
    (folder_path, port_number) = check_and_get_arguments()
    check_create_server_folder(folder_path)
    passwords = read_passwords('dfs.conf')
    serversocket = create_server_socket(port_number)

    print('Waiting for clients ' + folder_path + ' ' +  str(port_number))
    while True:
        (clientsocket, address) = serversocket.accept()
        print('Connected client ' + address[0] + ':' + str(address[1]))
        ct = threading.Thread(target=handle_client_connection, args=(clientsocket, passwords))
        ct.start()

    serversocket.close()