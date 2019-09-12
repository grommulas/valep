#Сервер
import socket

HOST = 'localhost'
PORT = 9091
sock = socket.socket()
sock.bind((HOST,PORT))
while True:
    sock.listen(1)
    conn,adr=sock.accept()

    text = 'Отправьте матрицу'
    conn.send(text.encode())

    text = conn.recv(65565).decode()
    if not text:
        break
    try:
        per = list(map(lambda x: x.strip().split(' '),text[1:-1].split(';')))
        det=float(per[0][0])*float(per[1][1])*float(per[2][2])+\
            float(per[0][1])*float(per[1][2])*float(per[2][0])+\
            float(per[0][2])*float(per[1][0])*float(per[2][1])-\
            float(per[0][2])*float(per[1][1])*float(per[2][0])-\
            float(per[0][0])*float(per[1][2])*float(per[2][1])-\
            float(per[0][1])*float(per[1][0])*float(per[2][2])
        dat="Определитель матрицы = "+str(det)
        conn.send(dat.encode())
    except ValueError:
     conn.send("Вы ввели неправильную матрицу".encode())