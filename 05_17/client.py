import socket

host = "127.0.0.1"
port = 8080
send = True
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_port = (host, port)
client_socket.connect(host_port)
while send:
    mess = input("Введите сообщение: ")
    client_socket.send(mess.encode())
    if mess.upper() == 'ВЫХОД':
        send = False
    else:
        recv_mess = client_socket.recv(1024).decode()
        print("Ответ: ", recv_mess)
client_socket.close()
