#exercise 1 function
def seq_ping():
    print("OK")

#exercise 2 function
def valid_filename():
    FOLDER = "./sequences/"
    exit = False
    while not exit:
        filename = input("What file do you want to enter?")
        try:
            f = open(FOLDER+filename+".txt", "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("This file has not been found")

def seq_read_fasta(filename):
    FOLDER = "./sequences/"
    seq = open(FOLDER+filename+".txt", "r").read()
    new_seq = seq.find("\n")
    seq = seq[new_seq:].replace("\n","")
    return seq


#exercise 3
def seq_len(seq):
    FOLDER = "./sequences/"
    data_list = []
    for g in seq:
        data_list.append(len((seq_read_fasta(g))))
    return data_list

def print_seq_len(data_list):
    print("-----| Exercise 3 |------\nGene U5--> Length:",data_list[0],
          "\nGene ADA --> Length:",data_list[1],
          "\nGene FRAT1 --> Length:",data_list[2],
          "\nGene FXN --> Length:",data_list[3])



#exercise 4
"""def seq_count_base(seq,base):
    total_bases_count = []
    for l in seq:
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        new_seq = seq_read_fasta(l)
        bases_count = []
        for c in range(0,len(new_seq)):
            if new_seq[int(c)]== base[0]:
                a_count += 1
            elif new_seq[int(c)] == base[1]:
                c_count += 1
            elif new_seq[int(c)] == base[2]:
                g_count += 1
            elif new_seq[int(c)] == base[3]:
                t_count += 1
        bases_count.append(a_count)
        bases_count.append(c_count)
        bases_count.append(g_count)
        bases_count.append(t_count)

        total_bases_count.append(bases_count)

    return total_bases_count



"""
def seq_count_base(seq,base):
    total_bases_count = []
    for l in seq:
        bases_count = [0,0,0,0]
        new_seq = seq_read_fasta(l)
        for c in range(0,len(new_seq)):
            if new_seq[int(c)]== base[0]:
                bases_count[0] += 1
            elif new_seq[int(c)] == base[1]:
                bases_count[1] += 1
            elif new_seq[int(c)] == base[2]:
                bases_count[2] += 1
            elif new_seq[int(c)] == base[3]:
                bases_count[3] += 1


        total_bases_count.append(dict(zip(base,bases_count)))

    return total_bases_count

def print_info_count(seq,total_bases_count):
    for l in range(0,len(seq)):
        print("Gene",seq[l],":")
        for key, value in total_bases_count[l].items():
            print(key,":",value)