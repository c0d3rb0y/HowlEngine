import socket
import threading


class Client:
    def __init__(self, messageC, *args):
        if messageC:
            self.create_connection()
        else:
            if args.__len__() > 0:
                print(args)
                self.create_connection_no_aio(args[0], args[1])

    def create_connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while 1:
            try:
                host = input('Enter host name --> ')
                port = int(input('Enter port --> '))
                self.s.connect((host, port))

                break
            except:
                print("Couldn't connect to server")

        message_handler = threading.Thread(target=self.handle_messages, args=())
        message_handler.start()

    def create_connection_no_aio(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        while 1:
            pass


    def create_connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while 1:
            try:
                host = input('Enter host name --> ')
                port = int(input('Enter port --> '))
                self.s.connect((host, port))
                self.s.send(b'CPacketJoin')
                break
            except:
                print("Couldn't connect to server")

        message_handler = threading.Thread(target=self.handle_messages, args=())
        message_handler.start()

    def handle_messages(self):
        while 1:
            print(self.s.recv(1204).decode())

    def input_handler(self):
        print("say exit to leave")
        while 1:
            a = input()
            if a != "exit":
                self.s.send((a).encode())
            else:
                self.leave_server()

    def send(self, input):
        self.s.send(input.encode())

    def leave_server(self):
        self.s.send(b"CPacketLeave")
        print("THERE IS NO PROBLEM THIS CRASHES ON PURPOSE")
        self.s.close()
        quit()

    def get_latest(self):
        return self.s.recv(1204).decode()


if __name__ == "__main__":
    client = Client(True)
    input_handler = threading.Thread(target=client.input_handler, args=())
    input_handler.start()

