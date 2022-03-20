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

names_sequences = ["U5","FRAT1","ADA"]
for s in names_sequences:
    s1 = Seq()
    s1.read_fasta(s)

    print("To Server: ", end="")
    termcolor.cprint(f"Sending {s} Gene to the server...", "blue")
    response1 = c.talk(f"Sending {s} Gene to the server...")
    print("From Server:\n")
    termcolor.cprint(response1, "green")

    print("\nTo Server: ", end="")
    response2 = c.talk(s1.strbases)
    termcolor.cprint(s1.strbases, "blue")
    print("From Server:\n")
    termcolor.cprint(response2 + "\n", "green")
