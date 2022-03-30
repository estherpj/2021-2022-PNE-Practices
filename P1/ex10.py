from Seq1 import Seq

PRACTICE = 1
EXERCISE = 10
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


list_sequences = ["U5","ADA","FRAT1","FXN","RNU6_269P"]

try:
    for s in list_sequences:
        s1 = Seq()
        s1.read_fasta(s)
        print("Gene",s,": Most frequent Base:",max(s1.seq_count_base(),key = s1.seq_count_base().get))
        #key parameter,it defines a function --> returns element
        #.get method to pop up the value assignated to that key
except FileNotFoundError:
    print("This file does not exist.")


