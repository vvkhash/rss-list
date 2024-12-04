import feedparser
from urllib.parse import urlparse,parse_qs


def get_rss(url_param):
    try:
        source = parse_qs(urlparse(url_param)[4])['source']
    except Exception:
        source = ["https://blog.vvkhash.com/rss.xml"]
    for s in source:
        feed = ''
        for e in get_feed_list(s)['entries']:
            feed += f"<p>{e['published']} / <a href=\"{e['link']}\" target=\"_blank\" >{e['title']}</a> </p>\n"

        # feed = feed + get_feed_list(s)['feed']['title']
    return str(feed)


def get_feed_list(url):
    return feedparser.parse(url)


if __name__ == "__main__":
    # Local debug
    # https://www.pythonforbeginners.com/feedparser/using-feedparser-in-python

    text = get_rss("https://blog.vvkhash.com/rss.xml?source=https://blog.vvkhash.com/rss.xml")
    print(text)
    exit(0)



