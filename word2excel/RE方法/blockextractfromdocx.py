import re
import docx
def extract_block(path_name):
    """逐行读取.docx,包含有名词解释的内容,提取出来,并返回字符串。

    Args:
        path_name (str): path_name为路径名+文件名
    """
    doc = docx.Document(path_name)  
    lines = list(doc.paragraphs)  #返回列表

    start_flag = '名词解释'
    store_flag = False
    # result = [] #输出列表
    result = '' #输出字符串

    for line in lines:
        if start_flag in line:
            store_flag = True
        elif store_flag and re.match(r'^\d+\．.*', line):
            # result.append(line.strip())
            result+=line
            # result+=line.strip()
        else:
            store_flag = False
    print('这是块读取结果：',result)
    return(result)
# print(result)
