from socket import *

# Server configuration
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the server to the specified IP address and port
serverSocket.bind(("127.0.0.1", serverPort))
print("The server is ready to receive")

while True:
    # Receive the filename from the client
    sentence, clientAddress = serverSocket.recvfrom(2048)
    filename = sentence.decode("utf-8")  # Decode the filename
    print(f"Requested file: {filename}")

    try:
        # Open the file and read its contents
        with open(filename, "r") as file:
            fileContents = file.read(2048)

        # Send the file contents back to the client
        serverSocket.sendto(fileContents.encode("utf-8"), clientAddress)
        print(f"Sent back to client: {fileContents}")
    except FileNotFoundError:
        # Handle case when the file is not found
        errorMessage = "File not found."
        serverSocket.sendto(errorMessage.encode("utf-8"), clientAddress)
        print(f"File '{filename}' not found. Sent error message to client.")
    except Exception as e:
        # Handle other exceptions
        errorMessage = f"An error occurred: {str(e)}"
        serverSocket.sendto(errorMessage.encode("utf-8"), clientAddress)
        print(f"An unexpected error occurred: {str(e)}")
