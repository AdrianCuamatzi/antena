# Sirve el escaneo wifi de Android (Termux + Termux:API) en http://localhost:8080
import subprocess, http.server

class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        out = subprocess.run(["termux-wifi-scaninfo"], capture_output=True, text=True).stdout or "[]"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(out.encode())
    def log_message(self, *a): pass

http.server.HTTPServer(("127.0.0.1", 8080), H).serve_forever()
