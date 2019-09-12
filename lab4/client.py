#Клиент
import socket

sock= socket.socket()
sock.connect(("localhost",9091))

print(sock.recv(1024).decode())

b = input('Введите матрицу в виде "[1 2 3; 4 5 6; 7 8 9]" ')
if len(b)>20:

    sock.send(b.encode())

    print(sock.recv(65565).decode())
    sock.close()
else:
    print("Вы ввели матрицу неправильного размера")
    b=str([1,2,3,4,5,6,7,8,9])
    sock.send(b.encode())
    print(sock.recv(65565).decode())
    sock.close()

