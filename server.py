import http.server
import socketserver
PORT = 8000
from http.server import SimpleHTTPRequestHandler



#text_file = open("index.html", "r")
#data = text_file.read()
#text_file.close()

class MyHandler(SimpleHTTPRequestHandler):
     def send_error(self, code, message=None):
         print('REACH')
         if code == 404:
             #self.error_message_format = data
             self.send_response(301)
             self.send_header('Location','http://localhost:8000')
             self.end_headers()
         SimpleHTTPRequestHandler.send_error(self, code, message)

httpd = socketserver.TCPServer(("", PORT), MyHandler)
print("serving at port", PORT)
httpd.serve_forever()
