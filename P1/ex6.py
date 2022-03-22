from Seq1 import Seq

PRACTICE = 1
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}"")", s1,
      "\n\tBases:",s1.seq_count_base())
print(f"Sequence 2: (Length: {s2.len()}"")",s2,
      "\n\tBases:",s2.seq_count_base())
print(f"Sequence 3: (Length: {s3.len()}"")", s3,
      "\n\tBases:",s3.seq_count_base())

