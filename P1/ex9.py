from Seq1 import Seq

PRACTICE = 1
EXERCISE = 9
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

try:
      s1 = Seq()
      s1.read_fasta("U5")
      print(f"Sequence: (Length: {s1.len()}"")", s1,
            "\n\tBases:",s1.seq_count_base(),
            "\n\tRev:",s1.seq_reverse(),
            "\n\tComp:",s1.seq_complement())

except FileNotFoundError:
      print("The file has not been found.")


