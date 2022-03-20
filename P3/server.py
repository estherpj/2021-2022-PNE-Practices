import socket
from Seq1 import Seq
from termcolor import colored

def info_operation():
    arg = split_list[1]
    response = "Sequence:" + arg + "\n"
    response += "Total length:" + str(seq.len()) + "\n"
    dictionary_bases = seq.percentages_bases()
    response += ""
    for k, v in dictionary_bases.items():
        response += k + ":" + str(v[0]) + "(" + str(round(v[1], 1)) + "%" + ")" + "\n"
    return response

def get_stringbases():
    arg = split_list[1]
    if arg == "0":
        response = "GET 0: ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA\n"
    elif arg == "1":
        response = "GET 1: AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA\n"
    elif arg == "2":
        response = "GET 2: CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT\n"
    elif arg == "3":
        response = "GET 3: CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA\n"
    elif arg == "4":
        response = "GET 4: AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT\n"
    return response


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)

        msg = msg_raw.decode().replace("\n", "").strip()
        split_list = msg.split(" ")

        cmd = split_list[0]
        print(colored(cmd, "green"))

        if cmd != "PING" and cmd != "GET":
            arg = split_list[1]
            seq = Seq(arg)

        if cmd == "PING":
            response = "OK\n"

        elif cmd == "GET":
            response = get_stringbases()
            print(response)

        elif cmd == "REV":
            response = seq.seq_reverse() + "\n"
            print(response)

        elif cmd == "INFO":
            response = info_operation()
            print(response)

        elif cmd == "COMP":
            response = seq.seq_complement() + "\n"
            print(response)

        elif cmd == "GENE":
            s1 = Seq()
            response = s1.read_fasta(str(arg))
            print(response)

        else:
            response = "This command is not available in the server.\n"

        cs.send(response.encode())
        cs.close()
