import socket
servak= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servak.bind(("localhost", 4444))

servak.listen(1)
print("Сервер очікує підключення")

info, ip_adress = servak.accept()
print(f"До мене під'єднався кліент с ip{ip_adress}")

data = info.recv(1024).decode()
print(data)

info.send(f"Привіт {data}".encode())

info.close()
servak.close()