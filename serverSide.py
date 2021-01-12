import socket
import tqdm

HOST = ''#input host ip
PORT = #input port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

client, address = server.accept()

while True:
    print(f"connected to {address}")
    cmd_input =  input("enter a command: ")
    client.send(cmd_input.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
