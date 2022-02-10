import seq0

filename = seq0.valid_filename()
sequence = seq0.seq_read_fasta(filename)
comple_dna = seq0.seq_complement(sequence[0:20])

print("Gene", filename +":")
print("Frag:",sequence[0:20])
print("Comp:",comple_dna)
