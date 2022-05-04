import http.server
import socketserver
import termcolor
import pathlib
import urllib.parse as u
import jinja2 as j
from Seq1 import Seq

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
HTML_FOLDER = "./html/"
LIST_SEQUENCES = ["AGTGGGAAATTTCCC", "GGTTAACCAAG","AGTTGACCAATT","CCAGTAGCTAAG", "AAAAAGGGCCCTTT"]
LIST_GENES = ["ADA", "FRAT1","FXN","U5","RNU6_269P"]

def read_html_file(filename):
    contents = pathlib.Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

def dictionary_data(dictionary,sequence):
    length_seq = len(sequence)
    result = ""
    for k,v in dictionary.items():
        result += k + ":" + str(v) + "\n"
    format_text = "Total length: " + str(length_seq) + "\n" + result
    return format_text

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
            contents = read_html_file("index.html").render(context={"n_sequences": len(LIST_SEQUENCES), "genes":LIST_GENES})
        elif path == "/ping":
            contents = read_html_file(path[1:]+".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0])
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:]+".html").render(context={"n_sequence": n_sequence, "sequence":sequence})
        elif path == "/gene":
            g_name = arguments["g_name"][0]
            sequence = pathlib.Path("./sequences/"+ g_name + ".txt").read_text()
            contents = read_html_file(path[1:] + ".html").render(context={"g_name":g_name, "sequence": sequence})
        elif path == "/operation":
            sequence = arguments["sequence"][0]
            seq = Seq(sequence)
            seq.valid_sequence1()
            operation = arguments["operation"][0]
            if operation == "Rev":
                seq_rev = seq.seq_reverse()
                contents = read_html_file(path[1:] + ".html").render(context={"operation": operation, "result": seq_rev, "sequence": seq})
            elif operation == "Comp":
                seq_comp = seq.seq_complement()
                contents = read_html_file(path[1:] + ".html").render(context={"operation": operation, "result": seq_comp, "sequence": seq})
            elif operation == "Info":
                seq_count = seq.seq_count_base()
                result = dictionary_data(seq_count,sequence)
                contents = read_html_file(path[1:] + ".html").render(context={"operation": operation, "result": result, "sequence": seq})

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


        #when u pass the string withh the html file, if you add /n you get everything in the line--> when create the string
        #need to have html format, you can write br or also put a <p> contents </p> --> should compile wity html not python