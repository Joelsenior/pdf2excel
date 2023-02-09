from pdfread import read_pdf_by_name
from out import write_2_excel
from pretreatment import pdf_str_pretreatment
from qestproccess import single_multiple_question, single_choice_question, all_question

if __name__ == '__main__':
    # pdf_str = read_pdf_by_name('./tiku.pdf')
    # pdf_str = read_pdf_by_name('./23肖秀荣1000题试题册.pdf')
    # pdf_str = read_pdf_by_name('./23肖秀荣1000题解析册.pdf')
    # print(pdf_str)

    # 读取文件，从新的题库
    pdf_str = ""
    with open("3.txt", "r", encoding="utf-8") as f:
        pdf_str = f.read()

    # # 获取pdf文档中各种题型的截取文字块
    # qest_map = pdf_str_pretreatment(pdf_str)
    # qest_map = txt_str_pretreatment(pdf_str)

    # # 处理单项选择题目
    # choice_question = single_choice_question(qest_map["choice_question_str"])
    # multiple_question = single_multiple_question(qest_map["multiple_question_str"])

    # 修改的方法
    question = all_question(pdf_str)

    # print(question)

    # # 导出Excel
    # write_2_excel([{"type": 1, "data": choice_question}, {"type": 2, "data": multiple_question}])
    write_2_excel(question)
