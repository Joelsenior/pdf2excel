# 预处理
def pdf_str_pretreatment(pdf_str):
    current_type = ""
    process_str = ""

    choice_question_str = ""
    multiple_question_str = ""
    material_question_str = ""

    for i in range(len(pdf_str)):
        item_str = pdf_str[i]

        # 最后一次循环
        if i == len(pdf_str) - 1:
            process_str += item_str
            if current_type == "单项选择题":
                choice_question_str += process_str
            elif current_type == "多项选择题":
                multiple_question_str += process_str
            elif current_type == "材料分析题":
                material_question_str += process_str
            break

        my_find_type = find_type(item_str)

        # 如果没有找到
        if my_find_type is None:
            # 待处理的文字
            process_str += item_str
            continue

        if current_type != my_find_type:
            if current_type == "单项选择题":
                choice_question_str += process_str
            elif current_type == "多项选择题":
                multiple_question_str += process_str
            elif current_type == "材料分析题":
                material_question_str += process_str

            current_type = my_find_type
            process_str = ""

    # print("----->单项选择")
    # print(choice_question_str)
    # print("----->多项选择")
    # print(multiple_question_str)
    # print("----->材料题")
    # print(material_question_str)
    # print("----->结束")
    return {
        "choice_question_str": choice_question_str,
        "multiple_question_str": multiple_question_str,
        "material_question_str": material_question_str
    }


def find_type(find_str):
    qest_list = ["单项选择题", "多项选择题", "材料分析题"]
    for q in qest_list:
        if find_str.find(q) >= 0:
            return q
    return None

