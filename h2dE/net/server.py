import socket
import threading

class Server:
    def __init__(self):
        self.start_server()

    def start_server(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        host = socket.gethostbyname(socket.gethostname())
        port = int(input('Enter port to run the server on --> '))

        self.clients = []

        self.s.bind((host,port))
        self.s.listen(100)
    
        print('Running on host: '+str(host))
        print('Running on port: '+str(port))

        while True:
            c, addr = self.s.accept()

            c.recv(1024).decode()
            
            print('New connection.')
            self.broadcast('SPacketAddUser')
            c.send("SPacketUsers".encode()+str(len(self.clients)).encode())

            self.clients.append(c)

            threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def broadcast(self,msg):
        for connection in self.clients:
            connection.send(msg.encode())

    def handle_client(self,c,addr):
        while True:
            try:
                msg = c.recv(1024)
            except:
                c.shutdown(socket.SHUT_RDWR)
                self.clients.remove(c)
                break

            if (msg.decode() != '')and(msg.decode() != 'CPacketLeave'):
                print(str(msg.decode()))
                for connection in self.clients:
                    if connection != c:
                        connection.send(msg)
            if (msg.decode() == 'CPacketLeave'):
                print("Client left.")
                c.shutdown(socket.SHUT_RDWR)
                self.clients.remove(c)
                self.broadcast("SPacketRemoveUser")
                break

server = Server()
