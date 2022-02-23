from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}"")", s1)
for key, value in s1.seq_count_base().items():
      print(key+":", value)

print(f"Sequence 2: (Length: {s2.len()}"")",s2)
for key, value in s2.seq_count_base().items():
      print(key + ":", value)

print(f"Sequence 3: (Length: {s3.len()}"")", s3)
for key, value in s3.seq_count_base().items():
      print(key + ":", value)
