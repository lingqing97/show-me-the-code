#random 库
#seed(a=None):初始化随机数种子
#>>seed(10) -》使用序号为10的种子序列
#random.random():返回[0.0,1.0)的一个数
#random.randint(a,b):返回[a,b]之间的一个整数
#random.uniform(a,b):返回[a,b]之间的随机小数
#random.choice(seq):返回序列seq中的一个元素
#>>random.choice([1,2,3,4,5,6,7,8,9])
#>>8
#random.shuffle(seq):将序列seq随机打乱
#>>random.shuffle(['abcd'])
#>>'bdca'
#string库
#string.ascii_uppercase:所有大写字母
#string.digits:所有数字
#range函数
#range(stop):返回[0,stop)的可遍历序列
#range(start,stop,step):生成一个步长为step的可遍历序列
import string 
import random
import sqlite3
def coupon_creator(digit):
    data=''
    for i in range(digit):
        data+=random.choice(string.ascii_uppercase+string.digits)
    return data
def coupons():
    conn=sqlite3.connect('coupon.db')
    c=conn.cursor()
    coupons=''
    count=1
    for count in range(1,201):
        digit=12 
        no='No.'+str(count)
        coupons=no+" "+coupon_creator(digit)
        c.execute("INSERT INTO coupon VALUES ('%s','%s')"%(no,coupons))
    conn.commit()
    conn.close()
if __name__=="__main__":
    coupons()
