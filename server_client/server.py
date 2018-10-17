from socket import socket
import time
import math

class Server:
    def __init__(self):
        self.connect = None
        self.srv = None

    def Open(self, port):
        if self.srv is not None:
            return

        self.srv = socket()
        self.srv.bind(('', port))
        self.srv.listen(1)

    def WaitClients(self):
        if self.srv is None:
            return

        self.connect, addr = self.srv.accept()
    
    def Send(self, message):
        if self.connect is None:
            return

        if type(message) is str:
            self.connect.send(message.encode())
        else:
            self.connect.send(message)
                

    def Read(self):
        if self.connect is None:
            return

        return self.connect.recv(1024)

    def Close(self):
        if self.connect is None:
             return

        self.connect.close()
        self.connect = None

if __name__ == '__main__':
    s = Server()
    s.Open(4548)
    print('Server start!')
    while True:
        print('Wait clients...')
        s.WaitClients()
        print('Client connect!')
        while True:
            data = s.Read()
            if data == b'':
                break
            
            a = data.decode().split()
            if hasattr(math, a[0]) and len(a) >= 2:
                method = getattr(math, a[0])
                s.Send(str(method(*map(lambda x: float(x), a[1:]))))
            else:
                s.Send(data)
            time.sleep(0.1)

    s.Close()