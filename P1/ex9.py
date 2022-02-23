from Seq1 import Seq
s1 = Seq()
s1.read_fasta("U5")
print(f"Sequence: (Length: {s1.len()}"")", s1,
      "\nBases:",s1.seq_count_base(),
      "\nRev:",s1.seq_reverse(),
      "\nComp:",s1.seq_complement())


