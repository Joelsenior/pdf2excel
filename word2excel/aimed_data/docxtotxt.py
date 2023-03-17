from docx2txt import process

def docxtotxt(filename):
    """
    filename:输入
    """
    try:
        # 读取.docx文件，并将其转换为纯文本
        text = process(filename)
        # 将文本保存到本地文件
        with open("newfilename.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"Error processing {filename}: {e}")
    return "newfilename.txt"

#测试用
if __name__ == "__main__":
    docxtotxt('test.docx')