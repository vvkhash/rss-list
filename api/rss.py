import feedparser
from urllib.parse import urlparse,parse_qs


def get_rss(url_param):
    try:
        source = parse_qs(urlparse(url_param)[4])['source']
    except Exception:
        source = ["https://blog.vvkhash.com/rss.xml"]
    for s in source:
        blog_style=" \" \
            font-family: Arial; \
            font-size: smaller; \
            color: gray; \
        \" "
        feed=""
        for e in get_feed_list(s)['entries']:
            date_list=e['published'].split(" ")
            date = f"{date_list[1]} {date_list[2]} {date_list[3]}"
            feed += f"<p style={blog_style}> <a href=\"{e['link']}\" target=\"_blank\" >{e['title']}</a> ({date}) </p>\n"
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

