from http.server import BaseHTTPRequestHandler
import feedparser

import urllib.request, urllib.parse, urllib.error
from urllib.parse import urlparse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))

        feed = get_feed_list("https://vvkhash.substack.com/feed")
        # self.wfile.write(str(feed).encode('utf-8'))
        self.wfile.write(feed['feed']['title'].encode('utf-8'))
        self.wfile.write("**************************** <br>".encode('utf-8'))

        o = urlparse(self.path)

        self.wfile.write(str(o).encode('utf-8'))
        return


def get_feed_list(url):

        return feedparser.parse(url)


if __name__ == "__main__":
    # Local debug
    # https://www.pythonforbeginners.com/feedparser/using-feedparser-in-python

    text = get_feed_list("https://vvkhash.substack.com/feed")
    exit (0)





