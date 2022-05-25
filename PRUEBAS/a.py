correct_sequence_gene = ""
                        n = 0
                        for i in sequence_gene:
                            correct_sequence_gene += i
                            n += 1
                            if n == 100:
                                correct_sequence_gene += "<br>"
                                n = 0


bases = "<br><br>"
                        for key, value in percentage_bases.items():
                            bases += key + " : " + str(value[0]) + ", " + str(round(value[1], 2)) + "%" + "<br>"