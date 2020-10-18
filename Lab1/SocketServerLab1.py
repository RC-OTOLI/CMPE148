from socket import *
import sys # In order to terminate the program


serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
port = 1010
serverSocket.bind(('', port))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.read()

        # Send one HTTP header line into socket
        connectionSocket.send(b'\nHTTP/1.1 200 OK\n\n')
        connectionSocket.send(outputdata.encode('utf-8'))

        # Send the content of the requested file to the client
        # for i in range(0, len(outputdata)):
        #     connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send(b'\nHTTP/1.1 404 Not Found\n\n')

        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
