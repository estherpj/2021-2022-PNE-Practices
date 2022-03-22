from Seq1 import Seq

PRACTICE = 1
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}"")", s1,
      f"\nSequence 2: (Length: {s2.len()}"")",s2,
      f"\nSequence 3: (Length: {s3.len()}"")", s3)