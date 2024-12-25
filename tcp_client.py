from socket import *

# Client configuration
serverName = "127.0.0.1"
serverPort = 12000

# Create a TCP socket and connect to the server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Input the filename from the user
filename = input("Enter file name: ")

# Send the filename to the server
clientSocket.send(filename.encode())

# Receive the file contents from the server
fileContents = clientSocket.recv(1024).decode()
print("From Server:", fileContents)

# Close the socket
clientSocket.close()
