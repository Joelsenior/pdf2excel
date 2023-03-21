import docx

doc = docx.Document('example.docx')

for paragraph in doc.paragraphs:
    text = paragraph.text
    print(text) # 包含换行符的整个段落文本
    for run in paragraph.runs:
        print(run.text) # 每个文本块的文本内容，不包含换行符