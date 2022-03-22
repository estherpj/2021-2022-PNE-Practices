from Seq1 import Seq

PRACTICE = 1
EXERCISE = 8
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
sequence_list = ["ACTGA","Invalid sequence"]

s1 = Seq()
print(f"Sequence 0: (Length: {s1.len()}"")",s1,
      "\n\tBases:",s1.seq_count_base(),
      "\n\tRev:",s1.seq_reverse(),
      "\n\tComp:",s1.seq_complement())

for s in sequence_list:
      s2 = Seq(s)
      print(f"Sequence",(sequence_list.index(s) + 1),f": (Length:{s2.len()})",s2,
      "\n\tBases:",s2.seq_count_base(),
      "\n\tRev:",s2.seq_reverse(),
      "\n\tComp:",s2.seq_complement())

