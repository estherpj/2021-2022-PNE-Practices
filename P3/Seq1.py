class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):

        # Initialize the sequence with the value
        # passed as argument when creating the object

        self.strbases = strbases
        if strbases == "NULL":
            print("NULL Seq Created")
        else:
            if not self.valid_sequence1():
                self.strbases = "ERROR"
                print("INVALID Seq!")
            else:
                print("New sequence created!")

    @staticmethod  # we can use this as a normal function
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def valid_sequence1(self):
        valid = True
        i = 0
        while i < len(self.strbases):
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def seq_count_base(self):
        bases_count = [0, 0, 0, 0]
        bases = ["A", "T", "C", "G"]
        if self.strbases == "NULL" or self.strbases == "ERROR":
            final_bases_count = dict(zip(bases, bases_count))
            return final_bases_count

        else:
            for c in range(0, len(self.strbases)):
                if self.strbases[int(c)] == bases[0]:
                    bases_count[0] += 1
                elif self.strbases[int(c)] == bases[1]:
                    bases_count[1] += 1
                elif self.strbases[int(c)] == bases[2]:
                    bases_count[2] += 1
                elif self.strbases[int(c)] == bases[3]:
                    bases_count[3] += 1
            final_bases_count = dict(zip(bases, bases_count))
            return final_bases_count

    def seq_reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            reversed_string = self.strbases[::-1]
            return reversed_string

    def seq_complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            comp_string = ""
            for i in range(0, len(self.strbases)):
                if self.strbases[i] == "A":
                    comp_string += "T"
                elif self.strbases[i] == "C":
                    comp_string += "G"
                elif self.strbases[i] == "G":
                    comp_string += "C"
                elif self.strbases[i] == "T":
                    comp_string += "A"
            return comp_string

    def read_fasta(self, filename):
        seq = open("./sequences/" + filename + '.txt', "r").read()
        new_seq = seq.find("\n")
        seq = seq[new_seq:].replace("\n", "")
        self.strbases = seq
        return seq

    def percentages_bases(self):
        diccionary = self.seq_count_base()
        sum_values = sum(diccionary.values())
        for k,v in diccionary.items():
            diccionary[k] = [v, (v*100)/sum_values]
        return diccionary








