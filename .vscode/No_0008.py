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
import requests,re
from bs4 import BeautifulSoup
def get_html_body(url):
   data=requests.get(url)
   pat=re.compile(r"^<body>[\s\S]*</body>")
   html=BeautifulSoup(data.text,'html.parser')
   r=pat.findall(html.prettify())
   print(r)
if __name__=="__main__":
    get_html_body('https://docs.python.org/3/')