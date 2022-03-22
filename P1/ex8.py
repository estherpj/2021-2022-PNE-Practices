from Seq1 import Seq

sequence_list = ["ACTGA","Invalid sequence"]

s1 = Seq()
print(f"Sequence 0: (Length: {s1.len()}"")",s1,
      "\nBases:",s1.seq_count_base(),
      "\nRev:",s1.seq_reverse(),
      "\nComp:",s1.seq_complement())

for s in sequence_list:
      s2 = Seq(s)
      print(f"\nSequence",(sequence_list.index(s) + 1),f": (Length:{s2.len()})",s2,
      "\nBases:",s2.seq_count_base(),
      "\nRev:",s2.seq_reverse(),
      "\nComp:",s2.seq_complement())

