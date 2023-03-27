import blockextract,blockextract_from_docx
import contentextract
import write_to_xlsx
path = r'test.docx' # 读取文本的路径
excel_file_path = 'zgt.xlsx'  #写入表格的路径
# aimed_block_string = blockextract.extract_block(path)  #提取目标块，此处为名词解释块，返回字符串
aimed_block_string = blockextract_from_docx.extract_block(path)  #提取目标块，此处为名词解释块，返回字符串
aimed_quest_list = contentextract.extract_content(aimed_block_string)  #提取内容，此处从名词解释块提取每段文字。
write_to_xlsx.write_to_xlsx(aimed_quest_list,excel_file_path)