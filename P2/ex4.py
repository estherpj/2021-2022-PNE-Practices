from Client0 import Client
from Seq1 import Seq
import termcolor

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")
s1 = Seq()
s1.read_fasta("U5")
s2 = Seq()
s2.read_fasta("FRAT1")
s3 = Seq()
s3.read_fasta("ADA")

sequences = [s1,s2,s3]
for s in sequences:
    s.talk(s.strbases)

print("To Server:")
termcolor.cprint(("Sending U5 Gene to the server..."),"blue")
response = c.talk("Testing!!!")
print("From Server:")
termcolor.cprint(response,"green")
