import http.server
import socketserver
import termcolor
import pathlib
import urllib.parse as u
import jinja2 as j
from Seq1 import Seq
import http.client
import json


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
HTML_FOLDER = "./html/"
SERVER = 'rest.ensembl.org'
ARGUMENT = "?content-type=application/json"

genes_dict = {"SRCAP": "ENSG00000080603","FRAT1": "ENSG00000165879","ADA":"ENSG00000196839",
              "FXN":"ENSG00000165060", "RNU6_269P":"ENSG00000212379","MIR633":"ENSG00000207552",
              "TTTY4C":"ENSG00000228296","RBMY2YP":"ENSG00000227633","FGFR3":"ENSG00000068078",
              "KDR":"ENSG00000128052 ","ANK2":"ENSG00000145362"}

def dic_info_server(url):
    conn = http.client.HTTPConnection(SERVER)
    parameters = "?content-type=application/json"
    try:
        conn.request("GET", url + parameters)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the server")
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    return data1


def read_html_file(filename):
    contents = pathlib.Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received! Request line:")
        termcolor.cprint("  " + self.requestline, 'green')
        url_path = u.urlparse(self.path)
        path = url_path.path
        arguments = u.parse_qs(url_path.query)

        print("  Command: " + self.command)
        print("  Path: " + self.path)

        if self.path == "/":
            contents = read_html_file("index.html").render()

        elif path == "/listSpecies":
            try:
                n_species = int(arguments["n_species"][0])
                dictionary_info = dic_info_server("info/species")
                species_info_list = dictionary_info["species"]
                species_list = []
                for i in species_info_list:
                    species_list.append(i["common_name"])

                correct_list_species = []
                for i in species_list:
                    if i not in correct_list_species:
                        correct_list_species.append(i)
                    else:
                        pass
                total_species = len(correct_list_species)
                species_html = "<br><br>"
                for n in correct_list_species[0:n_species]:
                    species_html += "<ul>" + "<li>" + " " + n + "<br>" + "</li>" + "</ul>"
                contents = read_html_file("listSpecies.html").render(context={"species": species_html,"total_species": total_species,"n_species": n_species})

            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/karyotype":
            species = arguments["specie"][0]
            dictionary_info_1 = dic_info_server("info/species")
            species_info_list = dictionary_info_1["species"]
            species_name = []
            for i in species_info_list:
                species_name.append(i["common_name"])
            if species not in species_info_list:
                contents = pathlib.Path("html/error.html").read_text()
            else:
                dic_specie = dic_info_server("info/assembly/" + species)
                karyotype = dic_specie["karyotype"]
                karyotype_html = "<br><br>"
                for n in karyotype:
                    karyotype_html += " " + n + "<br>"
                contents = read_html_file("karyotype.html").render(context={"karyotype": karyotype_html})

        elif path == "/chromosomeLength":
            species = arguments["specie"][0]
            chromosome = arguments["chromo"][0]

            dic_specie = dic_info_server("info/assembly/" + species)
            list_specie = dic_specie["top_level_region"]
            length = ""
            for i in list_specie:
                if i["name"] == chromosome:
                    length = i["length"]
            contents = read_html_file("chromosomeLength.html").render(context={"length": length})

        elif path == "/geneSeq":
            gene = arguments["gene"][0]
            dic_specie_gene = dic_info_server("lookup/symbol/homo_sapiens/"+gene)
            id_gene = dic_specie_gene["id"]
            dic_gene = dic_info_server("sequence/id/"+id_gene)
            sequence_gene = dic_gene["seq"]
            correct_sequence_gene = ""
            n = 0
            for i in sequence_gene:
                correct_sequence_gene += i
                n += 1
                if n == 100:
                    correct_sequence_gene += "<br>"
                    n = 0
            contents = read_html_file("gene.html").render(context={"gene": correct_sequence_gene})

        elif path == "/geneInfo":
            gene = arguments["gene"][0]
            dic_specie_gene = dic_info_server("lookup/symbol/homo_sapiens/" + gene)
            start_gene = dic_specie_gene["start"]
            end_gene = dic_specie_gene["end"]
            id_gene = dic_specie_gene["id"]
            length = int(end_gene) - int(start_gene)
            chromosome_name = dic_specie_gene["seq_region_name"]

            contents = read_html_file("infogene.html").render(context={"start": start_gene, "end": end_gene, "id_gene": id_gene,"chromosome": chromosome_name, "length": length})

        elif path == "/geneCalc":
            gene = arguments["gene"][0]
            id_gene = genes_dict[gene]
            dic_gene = dic_info_server("sequence/id/" + id_gene)
            sequence_gene = dic_gene["seq"]
            seq = Seq(sequence_gene)
            percentage_bases = seq.percentages_bases()
            bases = "<br><br>"
            for key, value in percentage_bases.items():
                bases += key + " : " + str(value[0]) + ", " + str(round(value[1], 2)) + "%" + "<br>"
                contents = read_html_file("calculusbases.html").render(context={"gene": gene, "calc_bases": bases})

        elif path == "/geneList":
            chromo = arguments["chromo"][0]
            start = arguments["start"][0]
            end = arguments["end"][0]
            info_chromo = chromo + ":" + start + "-" + end
            list_chromosome = dic_info_server("/phenotype/region/homo_sapiens/" + info_chromo)
            genes_found = []
            for i in list_chromosome:
                for n in i["phenotype_associations"]:
                    for e in n:
                        for c in e["attributes"]:


                    contents = read_html_file("chromo_genes.html").render(context={"chromo": chromo, "start": start, "end": end, "genes_found": genes_found})
        else:
            contents = pathlib.Path("html/error.html").read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(contents.encode())
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()