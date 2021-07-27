from Read_Excel import get_cell_data

def test_addition_two_string():
     str1=get_cell_data(8,1)

     str2=get_cell_data(8,2)
     print(str1+ " " +str2)