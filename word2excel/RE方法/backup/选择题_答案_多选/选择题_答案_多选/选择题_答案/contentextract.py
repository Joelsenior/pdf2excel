import re
from pip import main 
from blockextract_from_docx import extract_block
def extract_content(aimed_block):
    """形参接受字符串，通过正则表达式，最终print出来

    Args:
        aimed_block (str): 匹配"1．内皮："中"内皮"并打印。
    # """
    
    # pattern2_for_ques = r'\d+\．(.*?)[:\s]'  # pattern2_for_ques题目提取，根据:或者回车作为结尾符，读取。
    # pattern2_for_ans = r'\d+\．(.*?)\n'      # pattern2_for_ans答案提取，根据回车作为结尾符，读取。
    pattern2_for_ans = r'\d+[\.\．](.*?)\s'      # pattern2_for_ans题目提取，根据回车作为结尾符，读取。
    matches_for_ans  = re.findall(pattern2_for_ans,aimed_block)
    print('这是目标内容提取的结果： ',matches_for_ans)
    return matches_for_ans  #返回的是列表
    
##测试函数
if __name__ == '__main__': 
    A = extract_content(extract_block('test.docx'))   
