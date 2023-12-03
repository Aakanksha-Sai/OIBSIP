# Server (server.py)
import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.29.180", 12345))
    server.listen(1)
    print("Server is listening for incoming connections...")

    client, client_address = server.accept()
    print(f"Connected to {client_address}")

    while True:
        message = input("You: ")
        client.send(message.encode())
        received_message = client.recv(1024).decode()
        print(f"Client: {received_message}")

    client.close()

if __name__ == "__main__":
    start_server()
