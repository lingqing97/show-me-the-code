import xlwt
def write_worksheet(worksheet,file_data):
    city=eval(file_data)
    j=0
    for item in city.items():
        worksheet.write(j,0,int(item[0]))
        worksheet.write(j,1,item[1])
        j=j+1
if __name__=="__main__":
    workbook=xlwt.Workbook(encoding="ascii")
    worksheet=workbook.add_sheet("city_information")
    file_data=open(r'D:\360Downloads\GitHub客户端code\show-me-the-code\.vscode\city.txt','r',encoding='utf-8').read()
    write_worksheet(worksheet,file_data)
    workbook.save("./city.xls")