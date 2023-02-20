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

"""创建excel写入函数,接受数组ques、ans,和文件名excelname,并写入"""
def write2sheet(ques,ans,excelname):
    handbook = load_workbook('zgt.xlsx')
    excelname = excelname + '.xlsx'
    sheet = handbook.active
    nums = len(ques)
    for num in nums:
        ques_nums = 'b' + str(num)
        ans_nums = 'h' + str(num)
        sheet[ques_nums] = ques[num]
        sheet[ans_nums] = ans[num]
    handbook.save(excelname)
    print("数据写入成功！")
