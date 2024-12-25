from socket import *

# Server configuration
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the server to the specified IP and port
serverSocket.bind(("127.0.0.1", serverPort))
serverSocket.listen(1)  # Server listens for incoming connections
print("The server is ready to receive")

while True:
    # Accept a connection from the client
    connectionSocket, clientAddress = serverSocket.accept()
    print(f"Connection established with {clientAddress}")

    # Receive the filename from the client
    filename = connectionSocket.recv(1024).decode()
    print(f"Requested file: {filename}")

    try:
        # Open the file and read its contents
        with open(filename, "r") as file:
            fileContents = file.read()

        # Send the file contents to the client
        connectionSocket.send(fileContents.encode())
        print(f"Sent file contents to {clientAddress}")
    except FileNotFoundError:
        # Handle case when the file is not found
        errorMessage = "File not found."
        connectionSocket.send(errorMessage.encode())
        print(f"File '{filename}' not found. Sent error message to client.")

    # Close the connection with the client
    connectionSocket.close()
