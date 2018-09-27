# 通常利用哈希算法的单向性来保证明文以 不可还原的有损方式 进行存储。

# 这类方法的各个具体操作方式按安全性由低到高依次为：

# 1.使用自己独创的哈希算法对密码进行哈希，存储哈希过的值

# 哈希算法复杂，独创对理论要求很高。一般独创的哈希算法肯定没有公开经过时间检验的算法质量高，天才另算

# 2.使用 MD5 或 SHA-1 哈希算法

# MD5 和 SHA-1 已破解。虽不能还原明文，但很容易找到能生成相同哈希值的替代明文。而且这两个算法速度较快，暴力破解相对省时，建议不要使用它们。

# 3.使用更安全的 SHA-256 等成熟算法

# 更加复杂的算法增加了暴力破解的难度。但如果遇到简单密码，用彩虹字典的暴力破解法，很快就能得到密码原文

# 4.加入随机 salt 的哈希算法

# 密码原文（或经过 hash 后的值）和随机生成的 salt 字符串混淆，然后再进行 hash，最后把 hash 值和 salt 值一起存储。验证密码的时候只要用 salt 再与密码原文做一次相同步骤的运算，比较结果与存储的 hash 值就可以了。这样一来哪怕是简单的密码，在进过 salt 混淆后产生的也是很不常见的字符串，根本不会出现在彩虹字典中。salt 越长暴力破解的难度越大

# 具体的 hash 过程也可以进行若干次叠代，虽然 hash 叠代会增加碰撞率，但也增加暴力破解的资源消耗。就算真被破解了，黑客掌握的也只是这个随机 salt 混淆过的密码，用户原始密码依然安全，不用担心其它使用相同密码的应用。

# 上面这几种方法都不可能得到密码的明文，就算是系统管理员也没办法。对于那些真的忘了密码的用户，网站只能提供重置密码的功能了。

#常用的sha256加密算法:
# import hashlib
# hash_object = hashlib.sha256(b'Hello World')   ->注意：加密算法的输入为字节，所以要使用'b'前缀；
# hex_dig = hash_object.hexdigest()      —->将加密后的结果转化为16进制输出
# print(hex_dig)

#常用的获取salt的方法：
#import uuid
#salt=uuid.uuid4().hex
#hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt   ->加密后的结果

import uuid
import hashlib

def hash_password(password):
    salt=uuid.uuid4().hex
    return hashlib.sha256(salt.encode()+password.encode()).hexdigest()+":"+salt
def check_password(hash_password,user_password):
    password,salt=hash_password.split(":")
    return password==hashlib.sha256(salt.encode()+user_password.encode()).hexdigest()

if __name__=="__main__":
    password=input("please input your password:")
    hash_password=hash_password(password)
    user_password=input("please input your password again:")
    if check_password(hash_password,user_password):
        print("You enter the right password!")
    else:
        print("Sorry,the password is wrong!")