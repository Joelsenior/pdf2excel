import re 

def extract_content(aimed_block):
    """形参接受字符串，通过正则表达式，最终print出来

    Args:
        aimed_block (str): 匹配"1．内皮："中"内皮"并打印。
    # """
    
    # pattern2_for_ques = r'\d+\．(.*?)[:\s]'  # pattern2_for_ques题目提取，根据:或者回车作为结尾符，读取。
    # pattern2_for_ans = r'\d+\．(.*?)\n'      # pattern2_for_ans答案提取，根据回车作为结尾符，读取。
    pattern2_for_ans = r'\d+\．(.*?)\n'      # pattern2_for_ans答案提取，根据回车作为结尾符，读取。
    matches = re.findall(pattern2_for_ans, aimed_block)
    print('这是内容提取：',matches)
    return matches

    
##测试函数
# s = "细胞与组织\n一、名词解释\n1．内皮：\n2．间皮：\n3．微绒毛：\n4．纤毛：\n5．基膜：\n6．腺上皮:\n7．腺：\n8．内分泌腺：\n9．外分泌腺："
# extract_content(s)   
