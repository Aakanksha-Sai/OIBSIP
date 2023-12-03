# Client (client.py)
import socket

def start_client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345)) 

    while True:
        received_message = client.recv(1024).decode()
        print(f"Server: {received_message}")
        message = input("You: ")
        client.send(message.encode())

    client.close()

if(__name__=="__main__"):
    start_client()
