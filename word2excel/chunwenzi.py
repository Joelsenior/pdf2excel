from docx import Document
 
document=Document('rawdata.docx') #路径
all_paragraph=document.paragraphs
 
for paragraph in all_paragraph:
    print(paragraph.text)  #直接打印text即可
   # for run in paragraph.runs:   #这种方式有莫名其妙的换行
    #    print(run.text)