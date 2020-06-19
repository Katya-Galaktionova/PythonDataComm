import sys
import os
import socket
import hashlib
import threading


def check_and_get_arguments():
    if len(sys.argv) != 2:
        print('Error: must supply config file name\nUSAGE: ' +
              sys.argv[0] + ' dfc.conf')
        sys.exit()
    return sys.argv[1]


def create_client_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket


def check_servers_config(config_file_path):
    if not os.path.isfile(config_file_path):
        print('Config file ' + config_file_path + ' does not exist.')
        sys.exit()


def read_servers_config(config_file_path):
    servers = []
    username = ''
    password = ''
    fh = open(config_file_path)
    for line in fh:
        data = line.split()
        if len(data) != 0 and data[0].lower() == 'server':
            (host, port) = data[2].strip().split(':')
            servers.append((host, int(port)))
        else:
            data = line.split(':')
            if data[0].lower() == 'username':
                username = data[1].strip()
            elif data[0].lower() == 'password':
                password = data[1].strip()
    fh.close()
    return (servers, (username, password))


def print_config(servers, credentials):
    print('Servers')
    for server in servers:
        print(server[0] + ':' + str(server[1]))

    print('Credentials')
    print(credentials[0] + ':' + credentials[1])


def read_user_command():
    return input('Please provide command LIST, GET, PUT, EXIT: ')


def process_user_command(input, servers, credentials):
    data = input.split()
    command = data[0]
    if command.lower() == 'list':
        execute_list_command(servers, credentials)
    elif command.lower() == 'get':
        execute_get_command(data[1], servers, credentials)
    elif command.lower() == 'put':
        execute_put_command(data[1], servers, credentials)
    elif command.lower() == 'exit':
        print('Exiting')
        sys.exit()
    else:
        print('Not supported command:' + command)


def execute_get_command(file_name, servers, credentials):
    print('Executing get')


def execute_list_command(servers, credentials):
    print('Executing list')
    lists = []
    threads = []
    for i in range(4):
        t = threading.Thread(target=get_list, args=(
            servers[i], credentials, lists))
        threads.append(t)
        t.start()
    for i in range(4):
        threads[i].join()

    print('Servers have ' + lists)


def get_list(server, credentials, lists):
    client_socket = create_client_socket()
    client_socket.connect((servers[0], servers[1]))
    client_socket.send('list')
    list = client_socket.recv()
    client_socket.close()
    lists.append(list)


def execute_put_command(file_name, servers, credentials):
    print('Executing put ' + file_name)
    parts = read_file_parts(file_name)
    file_hash = int(calculate_hash(parts), 16) % 4

    threads = []
    for i in range(4):
        server_parts = choose_parts(file_hash, i)
        t = threading.Thread(target=send_parts, args=(
            servers[i], credentials, parts, server_parts))
        threads.append(t)
        t.start()
    for i in range(4):
        threads[i].join()


def choose_parts(hash, server_number):
    if hash == 0:
        if server_number == 0:
            return (0, 1)
        elif server_number == 1:
            return (1, 2)
        elif server_number == 2:
            return (2, 3)
        elif server_number == 3:
            return (3, 0)
    elif hash == 1:
        if server_number == 0:
            return (3, 0)
        elif server_number == 1:
            return (0, 1)
        elif server_number == 2:
            return (1, 2)
        elif server_number == 3:
            return (2, 3)
    if hash == 2:
        if server_number == 0:
            return (2, 3)
        elif server_number == 1:
            return (3, 0)
        elif server_number == 2:
            return (0, 1)
        elif server_number == 3:
            return (1, 2)
    elif hash == 3:
        if server_number == 0:
            return (1, 2)
        elif server_number == 1:
            return (2, 3)
        elif server_number == 2:
            return (3, 0)
        elif server_number == 3:
            return (0, 1)


def send_parts(server, credentials, file_name, all_parts, parts_to_send):
    print('Sending to ' + server[0] + ':' + str(server[1]))
    client_socket = create_client_socket()
    client_socket.connect((servers[0], servers[1]))
    put_message = 'put ' + file_name
    client_socket.send(put_message.encode())
    client_socket.send(str(parts_to_send[0]).encode())
    client_socket.send(all_parts[parts_to_send[0]])
    client_socket.send(''.encode())
    client_socket.send(str(parts_to_send[1]).encode())
    client_socket.send(all_parts[parts_to_send[1]])
    client_socket.send(''.encode())
    client_socket.close()


def calculate_hash(parts):
    hash = hashlib.md5()
    hash.update(parts[0])
    hash.update(parts[1])
    hash.update(parts[2])
    hash.update(parts[3])
    return hash.hexdigest()


def read_file_parts(file_name):
    if not os.path.isfile(config_file_path):
        print('File ' + file_name + ' does not exist')
        return []
    file_size = os.stat(file_name).st_size
    part_size = int((file_size - file_size % 4) / 4)
    last_part_size = int(part_size + file_size % 4)
    fh = open(file_name, 'rb')
    part1 = fh.read(part_size)
    part2 = fh.read(part_size)
    part3 = fh.read(part_size)
    part4 = fh.read(last_part_size)
    fh.close()
    return (part1, part2, part3, part4)


if __name__ == '__main__':
    config_file_path = check_and_get_arguments()
    check_servers_config(config_file_path)
    (servers, credentials) = read_servers_config(config_file_path)
    print_config(servers, credentials)

    while True:
        command = read_user_command()
        process_user_command(command, servers, credentials)
