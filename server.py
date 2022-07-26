import socket

srv_addr = input("Type the server IP address: ")
srv_port = int(input("Type the server port: "))

my_sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
my_sock.connect((srv_addr,srv_port))
print("connection established")

message = input("Message to send: ")
my_sock.sendall(message.encode())
my_sock.close