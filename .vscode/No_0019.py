import xlrd
from xml.dom import minidom

def open_xls(file,comment):
    workbook=xlrd.open_workbook(file)
    table=workbook.sheet_by_index(0)
    data=list()
    for i in range(3):
        data.append(table.row_values(i))
    write_xml(data,comment)

def write_xml(data,comment):
    doc=minidom.Document()
    root=doc.createElement('root')
    doc.appendChild(root)
    root_numbers=doc.createElement('numbers')
    root.appendChild(root_numbers)
    root_numbers.appendChild(doc.createComment(comment))
    root_numbers.appendChild(doc.createTextNode(str(data)))
    f=open('numbers.xml','w',encoding='utf-8')
    doc.writexml(f,newl='\n')

if __name__=="__main__":
    comment='数字信息'
    open_xls('D:\\360Downloads\\GitHub客户端code\\show-me-the-code\\numbers.xls',comment)