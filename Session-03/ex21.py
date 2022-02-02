def count_bases(seq): #name of the argument is something you can invent
    d = {"A":0,"C":0,"G":0,"T":0}
    for b in seq:
        d[b] += 1 #you are summing one to the value of this key
    return d

dna_seq = input("Introduce the sequence: ")
print("Total lenght:", len(dna_seq)) #we have that function so we do not need to put te
for k,v in count_bases(dna_seq).items():
    print(k + ":", v)

