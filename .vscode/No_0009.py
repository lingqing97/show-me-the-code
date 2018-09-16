import re
from bs4 import BeautifulSoup
def get_html_href(html):
    soup=BeautifulSoup(html)
    pat=re.compile("href=.*\s")
    hrefs=soup.find_all('a')
    for href in hrefs:
        fin_href=pat.findall(str(href))
        print(fin_href[0])
if __name__=="__main__":
    html_doc=open("./No_0009_html_doc.html").read()
    get_html_href(html_doc)