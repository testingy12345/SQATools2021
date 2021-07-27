import openpyxl
filepath="F:\\ToolsQAPython\\test_data.xlsx"
wb = openpyxl.load_workbook(filepath)

sheets=wb.worksheets
print(sheets)

print(sheets[0]._get_cell(1 ,1).value)

print(sheets[0]._get_cell(2 ,1).value)

print(sheets[0]._get_cell(2 ,2).value)

def get_cell_data(row,col,filepath=filepath):
    wb = openpyxl.load_workbook(filepath)
    sheets=wb.worksheets
    return sheets[0]._get_cell(row , col).value