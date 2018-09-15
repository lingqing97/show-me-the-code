#python.requests()
#使用get请求方式:
#res=requests.get(url)
#res.text:查看回应的内容
#使用put请求方式:
#res=requests.put(url)
#使用post请求方式:
#res=requests.post(url)
#pthon.bs4.BeautifulSoup
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link2">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>
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
import requests
from bs4 import BeautifulSoup
def get_html_body(html):
    soup = BeautifulSoup(html,'lxml')#如果不加入lxml，会提示错误
    print(soup.get_text())
if __name__=="__main__":
    get_html_body(html_doc)