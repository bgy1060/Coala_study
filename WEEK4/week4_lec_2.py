#openpyxl 연습하기

import openpyxl

wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']="Hello World"
sheet.cell(row=3,column=3).value="Good Bye"
sheet.append(['python','java','html','javascript'])
wb.save("test.xlsx")