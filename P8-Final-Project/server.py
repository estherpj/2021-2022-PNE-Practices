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

genes_dict = {"SRCAP": "ENSG00000080603", "FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296", "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"}


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

        l_json = 0
        if "json" in arguments.keys():
            if arguments["json"][0] == "1":
                l_json = 1

        print("  Command: " + self.command)
        print("  Path: " + self.path)

        if self.path == "/":
            contents = read_html_file("index.html").render()

        elif path == "/listSpecies":
            try:
                dictionary_info = dic_info_server("info/species")
                species_info_list = dictionary_info["species"]
                species_list = []
                for i in species_info_list:
                    species_list.append(i["name"])

                total_species = len(species_list)
                if "limit" not in arguments.keys():
                    n_species = total_species
                else:
                    n_species = int(arguments["limit"][0])
                if n_species < 0:
                    contents = pathlib.Path("html/error.html").read_text()
                else:
                    species_list_result = species_list[0:n_species]
                    if l_json == 0:
                        contents = read_html_file("listSpecies.html").render(context={"species": species_list_result,"total_species": total_species, "limit": n_species})
                    elif l_json == 1:
                        species_json = '{"species": ' + json.dumps(species_list_result) + "}"
                        contents = species_json

            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/karyotype":
            try:
                species = arguments["specie"][0]
                species = species.lower()
                if species.find(" ") != -1:
                    species = species.replace(" ", "_")

                dictionary_info_1 = dic_info_server("info/species")
                species_info_list = dictionary_info_1["species"]
                species_name = []
                for i in species_info_list:
                    species_name.append((i["name"]))
                if species not in species_name:
                    contents = pathlib.Path("html/error.html").read_text()
                else:
                    dic_specie = dic_info_server("info/assembly/" + species)
                    karyotype = dic_specie["karyotype"]
                    if len(karyotype) == 0:
                        karyotype_html = "no"
                        contents = read_html_file("karyotype.html").render(context={"karyotype": karyotype_html})
                    elif len(karyotype) != 0:
                        if l_json == 0:
                            contents = read_html_file("karyotype.html").render(context={"karyotype": karyotype})
                        elif l_json == 1:
                            karyotype_json = '{"karyotype": ' + json.dumps(karyotype) + "}"
                            contents = karyotype_json
            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/chromosomeLength":
            try:
                species = arguments["specie"][0]
                chromosome = arguments["chromo"][0]
                species = species.lower()
                if species.find(" ") != -1:
                    species = species.replace(" ", "_")

                dic_specie = dic_info_server("info/assembly/" + species)
                try:
                    list_specie = dic_specie["top_level_region"]
                    length = ""
                    for i in list_specie:
                        if i["name"] == chromosome:
                            length = i["length"]

                    if l_json == 0:
                        contents = read_html_file("chromosomeLength.html").render(context={"length": length})
                    elif l_json == 1:
                        lengthchromo_json = '{"lengthchromo": ' + json.dumps(length) + "}"
                        contents = lengthchromo_json
                except KeyError:
                    contents = pathlib.Path("html/error.html").read_text()
            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/geneSeq":
            try:
                gene = arguments["gene"][0]
                gene = gene.upper()
                dic_specie_gene = dic_info_server("lookup/symbol/homo_sapiens/"+gene)
                try:
                    id_gene = dic_specie_gene["id"]
                    dic_gene = dic_info_server("sequence/id/" + id_gene)
                    sequence_gene = dic_gene["seq"]

                    if l_json == 0:
                        contents = read_html_file("gene_seq.html").render(context={"gene": sequence_gene})
                    elif l_json == 1:
                        sequence_gene = list(sequence_gene)
                        contents = '{"geneSeq": ' + json.dumps(sequence_gene) + "}"
                except KeyError:
                    contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/geneInfo":
            try:
                gene = arguments["gene"][0]
                gene = gene.upper()
                dic_specie_gene = dic_info_server("lookup/symbol/homo_sapiens/" + gene) #to look for the id in ensembl instead of doing it with the dictionary
                try:
                    start_gene = dic_specie_gene["start"]
                    end_gene = dic_specie_gene["end"]
                    id_gene = dic_specie_gene["id"]
                    length = int(end_gene) - int(start_gene)
                    chromosome_name = dic_specie_gene["seq_region_name"]

                    if l_json == 0:
                        contents = read_html_file("infogene.html").render(context={"start": start_gene, "end": end_gene, "id_gene": id_gene,"chromosome": chromosome_name, "length": length})
                    elif l_json == 1:
                        keys_dict = ["start", "end", "id_gene", "length"]
                        info_gen = [start_gene, end_gene,id_gene, length ]
                        dict_info = json.dumps(dict(zip(keys_dict, info_gen)))
                        contents = dict_info
                except KeyError:
                    contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/geneCalc":
            try:
                gene = arguments["gene"][0]
                try:
                    id_gene = genes_dict[gene.upper()]
                    dic_gene = dic_info_server("sequence/id/" + id_gene)
                    sequence_gene = dic_gene["seq"]
                    seq = Seq(sequence_gene)
                    percentage_bases = seq.percentages_bases()

                    if l_json == 0:
                        contents = read_html_file("calculusbases.html").render(context={"gene": gene, "calc_bases": percentage_bases})
                    elif l_json == 1:
                        contents = json.dumps(percentage_bases)
                except KeyError:
                    contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/geneList":
            try:
                chromo = arguments["chromo"][0]
                start = arguments["start"][0]
                end = arguments["end"][0]
                info_chromo = chromo + ":" + start + "-" + end
                list_chromosome = dic_info_server("/phenotype/region/homo_sapiens/" + info_chromo)
                if len(list_chromosome) == 0:
                    contents = pathlib.Path("html/error.html").read_text()
                else:
                    try:
                        genes_found = []
                        for i in list_chromosome:
                            for n in i["phenotype_associations"]:
                                if "attributes" in n.keys():
                                    if "associated_gene" in n["attributes"]:
                                        genes_found.append(n["attributes"]["associated_gene"])

                            if len(genes_found) != 0:
                                if l_json == 0:
                                    contents = read_html_file("chromo_genes.html").render(context={"chromo": chromo, "start": start, "end": end, "genes_found": genes_found})
                                elif l_json == 1:
                                    genelist_json = '{"genes": ' + json.dumps(genes_found) + "}"
                                    contents = genelist_json
                            else:
                                genes_found = []
                                contents = read_html_file("chromo_genes.html").render(context={"chromo": chromo, "start": start, "end": end, "genes_found": genes_found})
                    except KeyError:
                        contents = pathlib.Path("html/error.html").read_text()
                    except TypeError:
                        contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

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