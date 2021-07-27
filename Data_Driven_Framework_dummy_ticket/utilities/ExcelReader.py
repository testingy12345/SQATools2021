import openpyxl

class Excel_Reader:
    def __init__(self ,file_path):
        self.filepath=file_path

    def read_excel_data(self,row,col,sheetname='Sheet1'):
        wb=openpyxl.load_workbook(self.filepath)
        sheet=wb[sheetname]
        data=sheet.cell(row,col).value
        return data


'''if __name__=="__main__":
    file_path="F:\\ToolsQAPython\\Data Driven Framework\\automation_framework\\data\\excel_files\\dummy_ticket.xlsx"
    obj=ExcelReader(file_path)
    print(obj.read_excel_data(1,1))
'''
