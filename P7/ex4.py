# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
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

try:
    ask_gene = input("Enter a gene name: ")
    URL = SERVER + ENDPOINT + genes_dict[ask_gene] + PARAMS
except KeyError:
    print("That key does not exist")
#do we need to put the server when using the request method? No we can use the endpoint+params

print(f"\nConnecting to server: {SERVER}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    try:
        conn.request("GET", ENDPOINT + genes_dict[ask_gene]+ PARAMS)
    except KeyError:
        print("That key does not exist")

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print("Server:", SERVER)
    print("URL", URL)
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1) #if the value of a key is an integer or a float it transforms it to a corresponding type.

    print("Gene:", ask_gene)
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