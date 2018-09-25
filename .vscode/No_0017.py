#python.xlrd模块:
#打开文件:
#workbook=xlrd.open_workbook(position)
#获取workbook中一个工作表:
#table=workbook.sheet_by_index(sheet_indx)  ->通过索引顺序获取
#table=workbook.sheet_by_name(sheet_name)   ->通过名称获取
#行的操作:
#nrows=table.nrows   ->获取该sheet的有效行数
#table.row_values(rowx,start_colx=0,end_colx=None)  ->返回该行中所有单元格的数据组成的列表
#列的操作:
#ncols=table.ncols  ->获取列表的有效列数
#table.col_values(colx,start_rowx=0,end_rowx=None)   ->返回由该列中所有单元格的数据组成的列表
#单元格的操作:
#table.cell_value(rowx,colx)  #返回rowx行，colx列的单元格中的数据
#python.xlrd模块:
#   import xml.dom.minidom
#   doc=minidom.Document()   ->创建xml文件
#    root=doc.createElement('employees')    ->创建根节点employees
#    doc.appendChild(root)  ->将root节点添加到xml文件中
#   employee = dom.createElement('employee')    ->创建子节点 employee
#   root.appendChild(employee)      ->将子节点 employee添加到root节点下
  
#   nameE=dom.createElement('name')     ->创建name节点
#   nameT=dom.createTextNode('linux')   ->创建文本内容'linux'
#   nameE.appendChild(nameT)    ->将文本内容'linux'添加到name节点中
#   employee.appendChild(nameE)     ->将节点name添加到employee节点下
  
#   ageE=dom.createElement('age')   ->创建age节点
#   ageT=dom.createTextNode('30')   ->创建文本内容'30'
#   ageE.appendChild(ageT)  ->将文本内容'30'添加到age节点中
#   employee.appendChild(ageE)  ->将age节点添加到root节点下
  

#   f= open('employees2.xml', 'w', encoding='utf-8')    ->以写的方式打开文件
#   dom.writexml(f, addindent='  ', newl='\n',encoding='utf-8')     ->将xml文件写到文件中
#   f.close() ->关闭文件

#运行结果:
# <?xml version="1.0" encoding="utf-8"?>
# <employees>
#   <employee>
#     <name>
#       linux
#     </name>
#     <age>
#       30
#     </age>
#   </employee>
# </employees>

#补充:
# from xml.dom import minidom
# doc=minidom.Document()
# root=doc.createElement('root')
# doc.appendChild(root)
# root.appendChild(doc.createComment('test'))  ->doc.createComment('test') 生成注释<!--test-->
# f=open('test.xml','w',encoding='utf-8')
# doc.writexml(f,newl='\n')
# print (doc)


import xlrd
from xml.dom import minidom

def open_xls(file,comment):
    workbook=xlrd.open_workbook(file)
    table=workbook.sheet_by_index(0)
    data=dict()
    for i in range(3):
        data.setdefault(str(i+1),(table.row_values(i,1,5)))
    write_xml(data,comment)

def write_xml(data,comment):
    doc=minidom.Document()
    root=doc.createElement('root')
    root_student=doc.createElement('student')
    doc.appendChild(root)
    root.appendChild(root_student)
    root_student.appendChild(doc.createComment(comment))
    root_student.appendChild(doc.createTextNode(str(data)))
    f=open('student.xml','w',encoding='utf-8')
    doc.writexml(f,newl='\n')

if __name__=="__main__":
    comment='    	学生信息表  "id" : [名字, 数学, 语文, 英文]'
    open_xls('D:\\360Downloads\\GitHub客户端code\\show-me-the-code\\student.xls',comment)
