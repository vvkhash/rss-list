from http.server import BaseHTTPRequestHandler
from api.rss import get_rss as get_feed



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # self.wfile.write('Hello, world!'.encode('utf-8'))
        feed = get_feed(self.path)
        self.wfile.write(feed['feed']['title'].encode('utf-8'))
        return
