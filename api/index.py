from http.server import BaseHTTPRequestHandler
from api.rss import get_rss # as get_feed



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        feed = get_rss(self.path)
        self.wfile.write(feed.encode('utf-8'))
        return
