import http.client
import json
from Seq1 import Seq

genes_dict = {"SRCAP": "ENSG00000080603","FRAT1": "ENSG00000165879","ADA":"ENSG00000196839",
              "FXN":"ENSG00000165060", "RNU6_269P":"ENSG00000212379","MIR633":"ENSG00000207552",
              "TTTY4C":"ENSG00000228296","RBMY2YP":"ENSG00000227633","FGFR3":"ENSG00000068078",
              "KDR":"ENSG00000128052 ","ANK2":"ENSG00000145362"}

SERVER = 'rest.ensembl.org'
ENDPOINT ='/sequence/id/'
PARAMS = "?content-type=application/json"


print(f"\nConnecting to server: {SERVER}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    for k,v in genes_dict.items():
        conn.request("GET", ENDPOINT + v + PARAMS)
        r1 = conn.getresponse()

        print("Server:", SERVER)
        print("URL", SERVER+ENDPOINT+v+PARAMS)
        print(f"Response received!: {r1.status} {r1.reason}\n")


        data1 = r1.read().decode("utf-8")
        data1 = json.loads(data1)

        print("Gene:", k)
        print("Description:", data1['desc'])
        seq = data1['seq']
        S = Seq(seq)
        print("Total lenght:",S.len())
        percentages_dic = S.percentages_bases()
        for k,v in percentages_dic.items():
            print(k +":",v[0],"(",round(v[1],1),"%)")

        number_bases = S.seq_count_base()
        values = list(number_bases.values())
        keys = list(number_bases.keys())
        freq_base = keys[values.index(max(values))]
        print("Most frequent base:", freq_base)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")