#collections.Counter():一个简单的计算器
#>>from collections import Counter
#>>c=Counter()
#>>for ch in 'programming':
#   c[ch]=c[ch]+1
#>>c
#Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
#>>c.items
#dict_items([('p', 1), ('r', 2), ('o', 1), ('g', 2), ('a', 1), ('m', 2), ('i', 1), ('n', 1)])
#re模块:
#'.':匹配除'\n'外的字符
#'*':匹配前一个字符0或多次
#'+':匹配前一个字符1或无限次
#'?':匹配前一个字符0或1次
#'^':匹配字符开头
#'$':匹配字符结尾
#'{m}':匹配字符m次,{m,n}匹配字符m到n次
#'\d':[0-9]
#'\s':匹配任何空白字符
#'\S':匹配任何非空白字符
#'\w':匹配包括下划线在内的任何字符[0-9a-zA-Z_]
#re.compile():返回一个正则表达式匹配模式（可以将常用的正则表达式编译成正则表达式对象，这样可以提高一点效率）
#re.match():从开头开始匹配
#re.search():从所有字符匹配，返回第一个满足的字符串
#re.findall():遍历匹配，返回字符串中所有匹配的字符串，返回一个列表
#re.match()和re.search()都返回一个匹配对象,匹配对象包含以下方法:
#group():返回匹配的字符串
#groups():返回匹配的所有子字符串
# import re
# pat=re.compile('(\d)([a-z])([A-Z])')
# print(re.match(pat,'1aD222sE')) #<_sre.SRE_Match object; span=(0, 3), match='1aD'>
# print(re.match(pat,'1aD222sE').group(0)) #1aD
# print(re.match(pat,'1aD222sE').group(1)) #1
# print(re.match(pat,'1aD222sE').groups()) #('1', 'a', 'D')
# print(re.search(pat,'1aD222sE').group()) #1aD
# print(re.findall(pat,'1aD222sE')) #[('1', 'a', 'D'), ('2', 's', 'E')]
#文件的读取
#open():打开文件
#read():读取整个文件，将其暂存为字符串
#readlines():返回一个行为单位的可迭代序列
#readline():一行一行读取文件
#close():关闭文件
import re
from collections import Counter
def words_counter(txt):
    c=Counter()
    pat=re.compile('[a-zA-Z_]+')
    words=re.findall(pat,txt)
    for word in words:
        c[word]=c[word]+1
    return c
if __name__=="__main__":
    txt=open('./No_0004_test.txt').read()
    print (words_counter(txt))