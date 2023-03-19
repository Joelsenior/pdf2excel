import pandas as pd
def write_to_xlsx(ques_list,excel_file_path):
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
    new_data = pd.DataFrame(ques_list) 
    
    # 将新数据写入Excel文件的E列
    try:
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a',if_sheet_exists = 'overlay') as writer: #续写Mode改为'a'
            # #从E(4列)列写入题目
            # new_data.to_excel(writer, sheet_name='Sheet1', startcol=4,startrow=1, index=False, header=False)  #head = flase 就是不用写表格头
            #从I(8列)列写入题目
            new_data.to_excel(writer, sheet_name='Sheet1', startcol=8,startrow=1, index=False, header=False)  #head = flase 就是不用写表格头
    except Exception as e:
        print(f"写入Excel文件时出错: {e}")
        return
    print("数据已成功写入Excel文件的E or I列！")
    
# 测试函数
if __name__ == '__main__': 
    data_list = [1, 2, 3, 4, 5]
    excel_file_path = 'zgt.xlsx'
    write_to_xlsx(data_list, excel_file_path)