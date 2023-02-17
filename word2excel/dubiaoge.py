from docx import Document
 
document=Document('rawdata.docx')
all_table=document.tables
 
for table in all_table:
   for row in table.rows:
       for cell in row.cells:
           print(cell.text) 