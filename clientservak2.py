import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1024))

# Потік для прийому повідомлень від сервера
def listen():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                print("\nСервер:", msg)
        except:
            pass

# Запускаємо "слухача"
thread = threading.Thread(target=listen).start()

# Цикл для відправки повідомлень
while True:
    message = input(": ")
    client.send(message.encode())
