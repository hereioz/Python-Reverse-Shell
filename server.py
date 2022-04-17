import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 4444))

print(s.recv(1024).decode('utf-8'))

while True:
    cmd = input("Shell: ")

    s.send(cmd.encode("utf-8"))

    recv = s.recv(1024).decode('utf-8')

    print(recv)