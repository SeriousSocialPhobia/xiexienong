import http.server
import socketserver

PORT = 19999
DIRECTORY = "D:\program\dist\dist"

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("Server started at localhost:", PORT)
httpd.serve_forever()