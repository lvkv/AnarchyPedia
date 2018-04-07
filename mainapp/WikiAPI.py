import xml.etree.ElementTree as ET
import requests

def get_article_HTML(article_title):
    WIKI_URL_PREFIX = "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&page="
    FORMAT_XML = "&format=xml"
    WIKI_QUERY_URL = WIKI_URL_PREFIX + article_title + FORMAT_XML

    r = requests.get(WIKI_QUERY_URL)
    root = ET.fromstring(r.content)
    html = root[0][0].text  # <api><parse><text>
    # print(html)
    return html

#get_article_HTML('pizza')