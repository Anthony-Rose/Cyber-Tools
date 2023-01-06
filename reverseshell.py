import socket
import subprocess
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create socket by binding locahost & port
server_address = ('localhost', 10000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for the client to connect
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive commands from the client
        while True:
            data = connection.recv(16)
            if data:
                # Pass the command to the operating system
                output = subprocess.run(data, shell=True, stdout=subprocess.PIPE)
                connection.sendall(output.stdout)
            else:
                print('no more data from', client_address)
                break
    finally:
        # Clean up the connection
        connection.close()
