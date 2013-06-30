import socket

s = socket.socket()
s.bind(('localhost', 13000))

s.listen(1)     #1 conexion

sc, addr = s.accept()   #en addr esta el host y el puerto de dicha conexion
print 'cliente conectado por: ',addr

while True:
    recibido = sc.recv(1024)
    print 'Recibido:', recibido
    if recibido == 'quit':
        break
    
print 'adios'
sc.close()
s.close()
