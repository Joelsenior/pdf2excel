"""从word中读取段落,并返回至一个列表"""
import docx
from openpyxl import load_workbook
def getText(fileName):
    doc = docx.Document(fileName)
    TextList = []
    for paragraph in doc.paragraphs:
        TextList.append(paragraph.text)

    return '\n'.join(TextList)

fileName = r'rawdata.docx'
print(getText(fileName))

"""创建excel文件,并写入"""
def write2sheet(ques,ans):
    handbook = load_workbook('zgt.xlsx')
    sheet = handbook.active
    nums = range(2, 53)
    for num in nums:
        ques_content = 'b' + str(num)
        ans_content = 'h' + str(num)
        sheet[ques_content] = ques
        sheet[ans_content] = ans
    handbook.save('zgt0217.xlsx')
    print("数据写入成功！")
