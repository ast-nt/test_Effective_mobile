from http.server import HTTPServer, BaseHTTPRequestHandler

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write('\"Hello from Effective Mobile!\"'.encode("utf-8"))

server_hostname = ""
server_port = 8080

if __name__ == "__main__":
    httpd = HTTPServer((server_hostname, server_port), AppHandler)
    httpd.serve_forever()