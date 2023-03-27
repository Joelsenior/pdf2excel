import pandas as pd
def write_to_xlsx(ques_choice_list,excel_file_path):
    """将列表读取，并写入到已经存在的列表zgt的E列。

    Args:
        ques_list (_type_): 列表
        excel_file_path:相对路径
    """
    try:
        df = pd.read_excel(excel_file_path, engine='openpyxl')
    except FileNotFoundError:
        print(f"文件路径 {excel_file_path} 不存在")
        return
    # 将数据列表转换为DataFrame
    # new_data = pd.DataFrame({'数据': ques_list})
    right_ans = pd.DataFrame([1]) 
    wrong_ans = pd.DataFrame([2])
    all_choice = {'A': 5, 'B': 8, 'C': 11, 'D': 14, 'E': 17, 'F': 20} 
    # 将新数据写入Excel文件的E列
    try:
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a',if_sheet_exists = 'overlay') as writer: #续写Mode改为'a'
            for index,ans in enumerate (ques_choice_list,start=1):
                list1 = []  #正确选项的value
                list2 = []  #不正确选项的value
                #获得匹配list
                for choice in all_choice:
                    if choice in ans:
                        list1.append(all_choice[choice])
                    else:
                        list2.append(all_choice[choice]) 
                print(list1,list2)                      
                for i in list1:    
                    right_ans.to_excel(writer, sheet_name='Sheet1', startrow=index,startcol=i, index=False, header=False)
                for j in list2:   
                    wrong_ans.to_excel(writer, sheet_name='Sheet1', startrow=index,startcol=j, index=False, header=False)
    except Exception as e:
        print(f"写入Excel文件时出错: {e}")
        return
    print("数据已成功写入Excel文件的多选题答案列！")
    
# 测试函数
if __name__ == '__main__': 
    data_list = [1, 2, 3, 4, 5]
    excel_file_path = '客观题.xlsx'
    write_to_xlsx(data_list, excel_file_path)