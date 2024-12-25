from socket import *

# Client configuration
serverName = "127.0.0.1"
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Input the filename from the user
filename = input("Enter file name: ")

# Send the filename to the server
clientSocket.sendto(filename.encode("utf-8"), (serverName, serverPort))

# Receive the response from the server
fileContents, serverAddress = clientSocket.recvfrom(2048)
print("From Server:", fileContents.decode("utf-8"))

# Close the socket
clientSocket.close()
