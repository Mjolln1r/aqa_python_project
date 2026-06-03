from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        self.wfile.write("Hello from myservice!\n".encode("utf-8"))


server = HTTPServer(("0.0.0.0", 8000), SimpleHandler)

print("Server started on http://localhost:8000")

server.serve_forever()