from http.server import HTTPServer, BaseHTTPRequestHandler
from  sympy import *
HOST ="localhost"
PORT = 8888
from m import *


class kHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", " text/html")
        self.end_headers()
        url = self.path
        operat(url)
        self.wfile.write(bytes("<html><body>url</body></html>", "utf-8"))

server = HTTPServer((HOST, PORT), kHTTP)
print("Server didnt die")
server.serve_forever()
server.serve_close()
print("Server stop")