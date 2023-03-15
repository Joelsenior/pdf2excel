import re
def extract_block(path_name):
    """将.txt中包含有名词解释的内容,提取出来,并返回字符串。

    Args:
        path_name (str): path_name为路径名+文件名
    """
    with open(path_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
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
