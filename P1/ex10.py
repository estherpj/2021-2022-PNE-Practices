from Seq1 import Seq
s1 = Seq()
s1.read_fasta("U5")
print("Gene U5: Most frequent Base:",max(s1.seq_count_base(),key = s1.seq_count_base().get))

s2 = Seq()
s2.read_fasta("ADA")
print("Gene ADA: Most frequent Base:",max(s2.seq_count_base(),key = s2.seq_count_base().get))

s3 = Seq()
s3.read_fasta("FRAT1")
print("Gene FRAT1: Most frequent Base:",max(s3.seq_count_base(),key = s3.seq_count_base().get))

s4 = Seq()
s4.read_fasta("FXN")
print("Gene FXN: Most frequent Base:",max(s4.seq_count_base(),key = s4.seq_count_base().get))

s5 = Seq()
s5.read_fasta("RNU6_269P")
print("Gene RNU6_269P: Most frequent Base:",max(s5.seq_count_base(),key = s5.seq_count_base().get))
