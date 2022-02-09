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
    list_genes = seq
    data_list = []
    for g in list_genes:
        data_list.append(len((seq_read_fasta(g))))
    return data_list

def print_seq_len(data_list):
    print("-----| Exercise 3 |------\nGene U5--> Length:",data_list[0],
          "\nGene ADA --> Length:",data_list[1],
          "\nGene FRAT1 --> Length:",data_list[2],
          "\nGene FXN --> Length:",data_list[3])




