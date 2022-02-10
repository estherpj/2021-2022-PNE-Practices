import seq0

filename = seq0.valid_filename()
sequence = seq0.seq_read_fasta(filename)
reverse_dna = seq0.seq_reverse(sequence[0:20])

print("Gene", filename +":")
print("Frag:",sequence[0:20])
print("Rev:",reverse_dna)