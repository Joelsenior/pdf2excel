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
    pattern2_for_ans = r'\d+\．(.*?)\n'      # pattern2_for_ans题目提取，根据回车作为结尾符，读取。
    patternA_for_choice = r'A\．(.*?)\s' #选项之间必须有空格或者回车，选项A前不能有空格。
    patternB_for_choice = r'B\．(.*?)\s'
    patternC_for_choice = r'C\．(.*?)\s'
    patternD_for_choice = r'D\．(.*?)\s'
    matches_of_quest = re.findall(pattern2_for_ans, aimed_block)
    matches_of_A = re.findall(patternA_for_choice, aimed_block)
    matches_of_B = re.findall(patternB_for_choice, aimed_block)
    matches_of_C = re.findall(patternC_for_choice, aimed_block)
    matches_of_D = re.findall(patternD_for_choice, aimed_block)
    print('这是题目提取：',matches_of_quest)
    print('这是选项A提取：',matches_of_A)
    print('这是选项B提取：',matches_of_B)
    print('这是选项C提取：',matches_of_C)   
    print('这是选项D提取：',matches_of_D)
    return matches_of_quest,matches_of_A,matches_of_B,matches_of_C, matches_of_D  #返回的是1*5 的 cell
    
##测试函数
if __name__ == '__main__': 
    A = extract_content(extract_block('test.docx'))   
