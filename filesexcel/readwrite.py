from xlwt import Workbook
from xlrd import open_workbook

"""
read
"""

wb = open_workbook('src.xls')
values = []
for s in wb.sheets():
    for row in range(s.nrows):
        for col in range(s.ncols):
            print s.cell(row,col).value
            values.append(s.cell(row,col).value)
            

"""
write
"""
suma=0
for element in values:
    suma=suma+element

book = Workbook()
sheet1 = book.add_sheet('Hoja 1')
book.add_sheet('Hoja 2')

sheet1.write(0,0,'Total')
sheet1.write(0,1,suma)

book.save('dst.xls')

print 'dst.xls created!'
