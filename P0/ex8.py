import seq0

seq = ["U5", "ADA","FRAT1","FXN"]
base = ["A","C","T","G"]
info_n_bases = seq0.seq_count_base(seq,base)
frequency_bases = seq0.most_frq_base(info_n_bases)
seq0.print_frequency_bases(seq, frequency_bases)