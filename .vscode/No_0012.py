class Input():
    def __init__(self):
        self.filter_words=list()
        self.in_txts=''
        self.out_txts=''
        self.load_filter_words()
    def load_filter_words(self,file='./filtered_words.txt'):
        lines=open(file,"r",encoding="utf-8").readlines() #若文档中有中文需指明编码方式为"utf-8"
        for line in lines:
            self.filter_words.append(line.strip()) #使用append()函数往list中添加新的元素
    def user_input(self):
        self.in_txts=input(">")
    def user_output(self):
        self.out_txts=self.in_txts
        for word in self.filter_words:
            if word in self.in_txts:
                self.out_txts=self.out_txts.replace(word,"*"*len(word))  #replace不会原地改变字符串，需要使用赋值运算改变字符串
    def user_prin(self):
        print(">"+self.out_txts)
if __name__=='__main__':
    inpu=Input()
    inpu.user_input()
    inpu.user_output()
    inpu.user_prin()