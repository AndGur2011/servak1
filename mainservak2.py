import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1024))
server.setblocking(False)
server.listen(5)
print("Работа")
clients = []

def accept_messages():
    while True:
        try:
            for client in clients:
                sended_message = client.recv(1024).decode()
                print(sended_message)
        except:
            pass
threading.Thread(target = accept_messages).start()
while True:
    try:
        information, ip_conect = server.accept()
        print("До мене підключився кліент:", ip_conect)
        information.setblocking(False)
        clients.append(information)
    except:
        pass
