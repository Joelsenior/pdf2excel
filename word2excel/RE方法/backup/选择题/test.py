# import docx

# doc = docx.Document('example.docx')

# for paragraph in doc.paragraphs:
#     text = paragraph.text
#     print(text) # 包含换行符的整个段落文本
#     for run in paragraph.runs:
#         print(run.text) # 每个文本块的文本内容，不包含换行符
from numpy import ones
import pandas as pd

# 读取现有的 Excel 文件
a = pd.read_excel('a.xlsx')

# 列名
columns = ['G', 'J', 'M', 'P']
choice_list = [1,2,3,4,5,6,7,8]
print(choice_list)
# 列索引
column_index = 0

# 将 choice_list 每四个一组分割成嵌套的列表
split_list = [choice_list[i:i+4] for i in range(0, len(choice_list), 4)]

# 将每个四元组写入到相应的列中
for group in split_list:
    for value in group:
        # 获取要填充的单元格的索引
        index = a.index.max() + 1
        # 将值填充到单元格中
        a.at[index, columns[column_index]] = value
        # 更新列索引
        column_index = (column_index + 1) % 4

# 将修改后的 DataFrame 保存到原始的 Excel 文件中
a.to_excel('a.xlsx', index=False)
