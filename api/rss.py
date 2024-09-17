import feedparser
from urllib.parse import urlparse,parse_qs


def get_rss(url_param):
    source = parse_qs(urlparse(url_param)[4])['source']
    feed = get_feed_list(source[0])
    # feed['feed']['title'] = feed['feed']['title']+"$$$"+str(urlparse(url_param))
    return feed


def get_feed_list(url):
    return feedparser.parse(url)


if __name__ == "__main__":
    # Local debug
    # https://www.pythonforbeginners.com/feedparser/using-feedparser-in-python

    text = get_rss("https://vvkhash.substack.com/feed?source=https://vvkhash.substack.com/feed")
    print(text)
    exit(0)





