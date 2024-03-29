import re
def extract_block(path_name):
    """将.txt中包含有名词解释的内容,提取出来,并返回字符串。

    Args:
        path_name (str): path_name为路径名+文件名
    """
    with open(path_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # print('这是逐行读取的内容：',lines)
    start_flag = '填空题'
    store_flag = False
    result = '' #输出字符串

    for line in lines:
        if start_flag in line:
            store_flag = True
        elif store_flag and re.match(r'^\d+．.*', line):  #匹配1.XX内容
            result+=line
        else:
            store_flag = False
    print('这是块读取结果：',result)
    return(result)

if __name__ == '__main__':
    extract_block(r'test.txt')
    