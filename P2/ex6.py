from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081

c = Client(IP, PORT1)
d = Client(IP, PORT2)
print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")
print(f"Connection to SERVER at {d.ip}, PORT: {d.port}")

s = Seq()
sequence = s.read_fasta("FRAT1")
print("Gene FRAT1:", s)
c.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
d.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")

i = 0
x = 10
count = 0
while i < 100:
    split_seq = sequence[i:x]
    i += 10
    x += + 10
    count += 1
    print(f"Fragment {count}: {split_seq}")
    if count % 2:
        c.talk(f"Fragment {count}: {split_seq}")
    else:
        d.talk(f"Fragment {count}: {split_seq}")