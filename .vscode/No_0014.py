#python.xlwt模块:使用python来处理excel
# 1、导入模块
# 　　import xlwt
# 2、创建workbook（其实就是excel，后来保存一下就行）
# 　　workbook = xlwt.Workbook(encoding = 'ascii')
# 3、创建表
# 　　worksheet = workbook.add_sheet('My Worksheet')
# 4、往单元格内写入内容
# 　　worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
# 5、保存
# 　　workbook.save('Excel_Workbook.xls')
import xlwt
import os,os.path
def write_file(worksheet):
    f=open(os.path.join(r"D:\360Downloads\GitHub客户端code\show-me-the-code\.vscode","student.txt"),"r",encoding="utf-8")
    _student=eval(f.read())
    student=list()
    for i in range(1,4):
        info=_student[str(i)]
        student.append(i)   #append函数将接受一个参数，将该参数作为一个整体添加到list尾部；
        student.extend(info)   #extend函数可接受一个可迭代对象，将该可迭代对象中的元素一个一个添加到list的尾部    
        for i in range(len(student)):
        worksheet.write(i//5,i%5,student[i])
if __name__=="__main__":
    file=xlwt.Workbook(encoding='ascii')
    worksheet=file.add_sheet('student information')
    write_file(worksheet)
    file.save('student.xls')