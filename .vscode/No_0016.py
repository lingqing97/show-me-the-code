import xlwt
def write_numbers(worksheet,file_data):
    numbers=eval(file_data)
    for i in range(3):
        for j in range(3):
            worksheet.write(i,j,numbers[i][j])
if __name__=="__main__":
    file_data=open(r"D:\360Downloads\GitHub客户端code\show-me-the-code\.vscode\numbers.txt","r",encoding="utf-8").read()
    workbook=xlwt.Workbook(encoding="ascii")
    worksheet=workbook.add_sheet("numbers")
    write_numbers(worksheet,file_data)
    workbook.save("./numbers.xls")
