from Session_06.Seq1 import Seq

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

for i in range(seq_list):
   print("Sequence", seq_list[i] + ":", ("Lenght:", len(seq_list[i])))
