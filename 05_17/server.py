import socket
host = "127.0.0.1"
port = 12345
listen = True
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bind_socket = (host, port)
server_socket.bind(bind_socket)
server_socket.listen(1)
print("Начало Прослушивания")
client_socket, addr = server_socket.accept()
print("Клиент: ", addr)
while listen:
    mess = client_socket.recv(1024).decode()

    if not mess:
        listen = False
        print("End listen!!")
    else:
        print("Получено: ", mess)
        client_socket.send("OK".encode())
client_socket.close()
server_socket.close()