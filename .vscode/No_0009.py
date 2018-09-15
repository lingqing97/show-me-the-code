html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re
from bs4 import BeautifulSoup
def get_html_href(html):
    soup=BeautifulSoup(html)
    hrefs=soup.find_all('a')
    pat=re.compile(r'^href="(.*)"$')
    for href in hrefs:
        res=pat.match(str(href))
        if res:
            print(res.group(1))
if __name__=="__main__":
    get_html_href(html_doc)