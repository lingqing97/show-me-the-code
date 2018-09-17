def is_sensitive_word(str):
    f=open("./filtered_words.txt","r",encoding="UTF_8")
    for line in f.readlines():
        if(str==line.strip()):
            return True
    return False
if __name__=="__main__":
    str=input("please input a string:")
    if(is_sensitive_word(str)):
        print("\nFreedom")
    else:
        print("\nHuman Rights")