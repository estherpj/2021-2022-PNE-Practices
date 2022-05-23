import http.client
import json
import socketserver

PORT = 8080
SERVER = '127.0.0.1'

conn = http.client.HTTPConnection(SERVER, PORT)
socketserver.TCPServer.allow_reuse_address = True

try:
    conn.request("GET", "/listSpecies?limit=10&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
print(data1)


"""try:
    conn.request("GET", "/karyotype?species=homo_sapiens&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)
print(data1)


try:
    conn.request("GET", "/chromosomeLength?species=homo_sapiens&chromosome=10&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)
print(data1)

try:
    conn.request("GET", "/geneSeq?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)
print(data1)

try:
    conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)
print(data1)

try:
    conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)
print(data1)

try:
    conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)
print(data1)

try:
    conn.request("GET", "/geneList?chromo=9&start=221225500&end=22136000&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)
print(data1)

try:
    conn.request("GET", "/geneList?chromo=9&start=221225500&end=22136000&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)
print(data1)"""




