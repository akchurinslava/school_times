import openpyxl
from operator import itemgetter
book = openpyxl.load_workbook("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/python/frontend/final/data.xlsx")

sheets=book.worksheets
sheet = book.active
sheet_2=book.worksheets[1]
sheet_3=book.worksheets[2] 

abc=[4,5,6]
#sorted_abc=dict(sorted(abc.items(), key=itemgetter(1)))
row=1
row2=1

for i in abc:
    sheet_2[row2][2].value=i
    row2+=1


#for i in abc.values():
   # sheet_2[row][1].value=i
   # row+=1




book.save("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/python/frontend/final/data.xlsx")
book.close


