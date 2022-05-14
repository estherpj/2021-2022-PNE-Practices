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
            n_species = arguments["n_species"]
            dictionary_info = dic_info_server("info/species")
            species_list = dictionary_info["species"]
            species_list = species_list[0:n_species]
            contents = read_html_file("html/listSpecies.html").render(context={"species":species_list})

        #elif path == "/karyotype":


        #elif path == "/chromosomeLength":


        else:
            contents = pathlib.Path("html/error.html").read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(contents.encode())
        return

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()