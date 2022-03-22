from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)


#PING
print("* Testing PING...")
msg = c.talk("PING")
print(msg)

#GET
print("* Testing GET 0...")
msg = c.talk("GET 0")
print(msg)

print("* Testing GET 1...")
msg = c.talk("GET 1")
print(msg)

print("* Testing GET 2...")
msg = c.talk("GET 2")
print(msg)

print("* Testing GET 3...")
msg = c.talk("GET 3")
print(msg)

print("* Testing GET 4...")
msg = c.talk("GET 4")
print(msg)

#INFO
print("\n* Testing INFO...")
msg = c.talk("INFO ATGA")
print(msg)

#COMP
print("* Testing COMP...")
msg = c.talk("COMP ATGA")
print(msg)

#REV
print("* Testing REV...")
msg = c.talk("REV ATGA ")
print(msg)

#GENE
print("* Testing GENE...")
msg = c.talk("GENE U5")
print(msg)