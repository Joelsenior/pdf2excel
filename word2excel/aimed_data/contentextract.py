import re 

def extract_content(aimed_block):
    """形参接受字符串，通过正则表达式，最终print出来

    Args:
        aimed_block (str): 匹配"1．内皮："中"内皮"并打印。
    # """
    # pattern1 = r'\d+．(.+?)：'
    # pattern2 = r'\d+．(.*?)(?:m|：)' #可以设计m和：为结束标志
    # pattern2 = r'\d+．([^：\s]+)[：\s]'
    pattern2 = r'\d+．(.*?)[:\s]'
    matches = re.findall(pattern2, aimed_block)
    # result = [r.rstrip(':') for r in matches]
    print('这是内容提取：',matches)
# s = "细胞与组织\n一、名词解释\n1．内皮：\n2．间皮：\n3．微绒毛：\n4．纤毛：\n5．基膜：\n6．腺上皮:\n7．腺：\n8．内分泌腺：\n9．外分泌腺："
# extract_content(s)   
