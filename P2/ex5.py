from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")

s = Seq()
sequence = s.read_fasta("FRAT1")
print("Gene FRAT1:", s)
c.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")

i = 0
x = 10
count = 0
while i < 50:
    split_seq = sequence[i:x]
    i += 10
    x += + 10
    count += 1
    print(f"Fragment {count}: {split_seq}")
    c.talk(f"Fragment {count}: {split_seq}")
