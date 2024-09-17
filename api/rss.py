import feedparser
from urllib.parse import urlparse,parse_qs


def get_rss(url_param):
    try:
        source = parse_qs(urlparse(url_param)[4])['source']
    except Exception:
        source = ["https://vvkhash.substack.com/feed"]
    feed = ''
    for s in source:
        feed = feed + get_feed_list(s)['feed']['title']
    return str(feed)


def get_feed_list(url):
    return feedparser.parse(url)


if __name__ == "__main__":
    # Local debug
    # https://www.pythonforbeginners.com/feedparser/using-feedparser-in-python

    text = get_rss("https://vvkhash.substack.com/feed?source=https://vvkhash.substack.com/feed&source=https://tty.vvkhash.com/data/rss")
    print(text)
    exit(0)



