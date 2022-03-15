import socket

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "127.0.0.1" #be careful with IP!!

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().replace("\n", "").strip() #we remove spaces to the left and to the right
        splitted_command = msg.split(" ")
        cmd = splitted_command[0]
        print(f"Message received: {msg}")
        if cmd != "PING":
            arg = splitted_command[1]
        print(f"Message received: {msg}")
        if cmd == "PING":
            response = "OK!\n"
        else:
            response = "This command is not available in the server.\n"
        cs.send(response.encode())
        cs.close()

#we have to run the server when we make a change in it