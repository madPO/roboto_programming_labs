from socket import socket

class Client:
    def __init__(self):
        self.connect = None

    def Open(self, host, port):
        if self.connect is not None:
            return

        self.connect = socket()
        self.connect.connect((host, port))

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
    c = Client()
    c.Open('localhost', 4548)
    while True:
        msg = input()
        if msg == 'close':
            break
        c.Send(msg)
        data = c.Read()
        print(data.decode())
        if data == b'':
            break
    c.Close()