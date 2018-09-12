#python strip():函数用于移除字符串首尾指定字符或字符序列(默认值为去除首尾空格)
# str = "00000003210Runoob01230000000"
# print (str.strip( '0' ))  # 去除首尾字符 0
# >>3210Runoob0123
# str2 = "   Runoob      "  # 去除首尾空格
# print (str2.strip())
# >>Runoob
# str = "123abcrunoob321"
# print (str.strip( '12' ))  # 字符序列为 12
# >>3abcrunoob3
import os,os.path
import re
def lines_count(path):
    files=os.listdir(path)
    pat=re.compile(r'^#.*')
    print ("file\all_lines\tspace_lines\texp_lines")
    for file in files:
        if os.path.splitext(file)[1]=='.py':
            all_lines=0
            space_lines=0
            exp_lines=0 
            f=open(file,'r', encoding='UTF-8')
            for line in f.readlines():
                all_lines=all_lines+1
                if str(line.strip())=='':
                    space_lines=space_lines+1
                    continue
                exp=pat.findall(str(line.strip()))
                if exp:
                    exp_lines=exp_lines+1
            print("%s\t%d\t%d\t%d\n"%(file,all_lines,space_lines,exp_lines))
if __name__=="__main__":
    lines_count(r'D:\360Downloads\GitHub客户端code\show-me-the-code\.vscode')