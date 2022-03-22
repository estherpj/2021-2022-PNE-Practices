from Seq1 import Seq

list_sequences = ["U5","ADA","FRAT1","FXN","RNU6_269P"]

try:
    for s in list_sequences:
        s1 = Seq()
        s1.read_fasta(s)
        print("Gene",s,": Most frequent Base:",max(s1.seq_count_base(),key = s1.seq_count_base().get))

except FileNotFoundError:
    print("This file does not exist.")


