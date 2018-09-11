from collections import Counter
import os.path,os
import re
def most_important_words_count(infiles):
    files=os.listdir(infiles)
    result=open('./No_0006.txt','w')
    for file in files:
        c=Counter()
        if os.path.splitext(file)[1]=='.txt':
            file_open=open(os.path.join(infiles,file)).read()
            pat=re.compile('[a-zA-Z_]+')
            words=pat.findall(file_open)
            for word in words:
                c[word]=c[word]+1
        max=0
        for item in c.items():
            if(item[1]>max):
                max=item[1]
                result_key=item[0]
        result.write(os.path.splitext(file)[0]+':   '+result_key+'\n')
        
if __name__=="__main__":
    most_important_words_count(r'D:\360Downloads\GitHub客户端code\show-me-the-code\.vscode\No_0006_test_txt')
