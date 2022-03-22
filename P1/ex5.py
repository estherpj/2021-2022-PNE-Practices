from Seq1 import Seq

PRACTICE = 1
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}"")", s1)
for key, value in s1.seq_count_base().items():
      print("\t"+key+":", value, ",", end="")

print(f"\nSequence 2: (Length: {s2.len()}"")",s2)
for key, value in s2.seq_count_base().items():
      print("\t"+ key + ":", value, ",",end="")

print(f"\nSequence 3: (Length: {s3.len()}"")", s3)
for key, value in s3.seq_count_base().items():
      print("\t"+ key + ":", value, ",", end="")
