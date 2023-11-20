from http.server import HTTPServer, BaseHTTPRequestHandler
from sympy import *
from my import *
HOST ="localhost"
PORT = 8888

a=0
class kHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", " text/html")
        self.end_headers()
        url = self.path
        operat(url)
        if(a==0):
            self.wfile.write(bytes("<html><body>Ramil?</body></html>", "utf-8"))

server = HTTPServer((HOST, PORT), kHTTP)
print("Server didnt die")
server.serve_forever()
server.serve_close()
print("Server stop")