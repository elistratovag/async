import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('192.168.1.110', 5000))
server_socket.listen()


while True:
        print("before accept()")
        client_socket, addr = server_socket.accept()
        print("Connected from: {}".format(addr))

        while True:
                print("before recv()")
                request = client_socket.recv(4096)

                if not request:
                        break
                else:
                        print("before send()")
                        response = "Hello, world!\n".encode()
                        client_socket.send(response)

        print("Outside inner while loop")
        client_socket.close()

