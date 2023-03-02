# # import docx
# # from openpyxl import Workbook

# # # 打开Word文档
# # doc = docx.Document('刷图库_题目.docx')

# # # 创建Excel工作簿
# # wb = Workbook()
# # ws = wb.active

# # # 遍历Word文档中的所有段落
# # for paragraph in doc.paragraphs:
# #     # 获取段落文本
# #     text = paragraph.text
    
# #     # 如果段落以“一、名词解释”开头，就提取名词列表
# #     if text.startswith('一、名词解释'):
# #         # 将段落文本按行分割
# #         lines = text.split('\n')
        
# #         # 遍历每行文本，提取名词并写入Excel
# #         for i, line in enumerate(lines):
# #             if i > 0:
# #                 # 获取名词
# #                 term = line.split('：')[0]
                
# #                 # 将名词写入Excel
# #                 cell = ws.cell(row=i, column=1)
# #                 cell.value = term

# # # 保存Excel文件
# # wb.save('your_excel_file.xlsx')

# import docx
# import re
# from openpyxl import Workbook

# # 打开Word文档
# doc = docx.Document('aimed_data\\刷题库_答案.docx')

# # 创建Excel工作簿
# wb = Workbook()
# ws = wb.active

# # 编译正则表达式模式
# # pattern = re.compile(r'^\d+、名词解释$')
# # pattern = re.compile(r'^\d+\.')
# # 构造正则表达式
# # pattern = re.compile(r'/、名词解释[\s\S]*?\n\n/')
# pattern = re.compile(r'/、名词解释(.*?)\n\n/')

# # 遍历Word文档中的所有段落
# for paragraph in doc.paragraphs:
#     # 获取段落文本
#     text = paragraph.text
#     # print(text)
#     # 如果段落匹配名词解释的正则表达式，就提取名词列表
#     # if pattern.match(text):
#     if pattern.match(text):
#         print("love")
#         # 将段落文本按行分割
#         lines = text.split('\n')
#         print(lines)
#         print("********************hello")
#         # 遍历每行文本，提取名词并写入Excel
#         for i, line in enumerate(lines):
#             if i >= 0:
#                 # 获取名词
#                 term = line.split('：')[0]
                
#                 # 将名词写入Excel
#                 cell = ws.cell(row=i, column=1)
#                 cell.value = term

# # 保存Excel文件
# wb.save('your_excel_file.xlsx')
import re
strofans = '''
一、名词解释
1.解剖学姿势：为说明人体局部或器官及结构的位置关系而规定的一种姿势，即身体 直立，面向前，两眼向正前方平视，两足并拢，足尖向前，上肢下垂于躯干两侧，掌 心向前。
2.冠状面：按左右方向，将人体分为前、后两部的纵切面，也叫额状面。
3.矢状面：按前后方向，将人体分为左、右两部的纵切面，
4.纵切面：指与器官长轴平行的切面。
5.横切面：指与器官长轴垂直的切面。
6.嗜酸性：是细胞和组织内的碱性物质或结构与酸性染料亲合力强者。
二、填空题
1.向前、向前
2.九、运动系统、消化系统、呼吸系统、泌尿系统、生 殖系统、脉管系统、感觉器、内分泌系统和神经系统
3.头、颈、躯干、四肢
4.水平面、矢状面、冠状面
5.纵切面、横切面、内侧、外侧、垂直轴、矢状轴、冠状轴
6.水平面、矢状面、冠状面
'''
result = re.findall(r'、名词解释(.*?)',strofans,re.S)
print(result)