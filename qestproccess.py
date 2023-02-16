import re


def single_choice_question(pdf_str):
    # 过滤不需要的文字块
    filter_split = beforehand(pdf_str)

    # 获取题干

    result = []

    for item in filter_split:
        find_a = item.find("A")
        if find_a <= 0:
            continue

        # 题干
        stem = item[0:find_a].replace("\n", "")

        qest = item[find_a:]

        # 抽离选项
        pattern = re.compile("A\\.|B\\.|C\\.|D\\.|A|B|C|D")

        re_split = pattern.split(qest)
        temp_re_split = []

        for r in re_split:
            new_r = str.strip(r).replace(".", "").replace("\n", "")
            if new_r != "":
                temp_re_split.append(new_r)

        # 去除空船和字符
        re_split = temp_re_split

        result.append({
            "stem": stem,
            "qest": re_split
        })

    return result


def single_multiple_question(pdf_str):
    return single_choice_question(pdf_str)


def beforehand(pdf_str):
    # 去除首尾空格
    pdf_str = str.strip(pdf_str)

    re_compile = re.compile('[0-9]+\.')
    split = re_compile.split(pdf_str)
    print(split)

    # 过滤不需要的文字块
    filter_split = []

    for s in split:
        if s.find("A") < 0 and s.find("a") < 0:
            continue
        filter_split.append(s)

    return filter_split


# 解析规则
def all_question(txt_str):
    # 预处理
    filter_split = beforehand(txt_str)

    # 单选题集合
    choice_question = []

    # 多选题集合
    multiple_question = []

    for f in filter_split:
        find_a = f.find("A")

        # 构建返回对象
        r = {
            "stem": None,
            "qest": [],
            "source": None,
            "answer": [],
            "analysis": None
        }
        if find_a <= 0:
            continue

        r["stem"] = str.strip(f[0:find_a])

        # 查找出处
        find_where = f.find("【出处】")

        if find_where <= 0:
            continue

        # 选项块
        qest = f[find_a:find_where]

        # 抽离选项
        pattern = re.compile("A\\.|B\\.|C\\.|D\\.|A|B|C|D")

        re_split = pattern.split(qest)

        # 拆分题目
        for re_item in re_split:
            re_item = str.strip(re_item)
            re_item = re_item.replace("\n", "")
            if re_item != "":
                r["qest"].append(re_item)

        find_source = f.find("【出处】")
        find_answer = f.find("【答案】")
        find_analysis = f.find("【简析】")
        find_dialing = f.find("【点拨】")

        # 出处
        r["source"] = f[find_source + 4:find_answer].replace("\n", "")

        # 答案
        answer = f[find_answer + 4:find_analysis].replace("\n", "").replace("选项", "").replace(
            "、", ",")
        answer_find = answer.find("【点拨】")
        if answer_find > 0:
            answer = answer[0:answer_find]

        r["answer"] = answer
        # if find_analysis < 0 and find_dialing < 0:
        #     r["answer"] = f[find_answer + 4:].replace("\n", "").replace("选项", "").replace(
        #         "、", ",")
        # else:
        #     r["answer"] = f[find_answer + 4:max(find_analysis, find_dialing)].replace("\n", "").replace("选项",
        #                                                                                                 "").replace(
        #         "、", ",")

        # 兼容处理
        # print(str(find_answer) + " " + str(find_analysis) + " " + str(find_dialing))
        if find_analysis > 0 and find_dialing > 0:
            r["analysis"] = f[min(find_analysis, find_dialing) + 4:].replace("\n", "").replace("【简析】", "").replace(
                "【点拨】", "")
        elif find_analysis > 0 > find_dialing:
            r["analysis"] = f[find_analysis + 4:].replace("\n", "").replace("【简析】", "")
        elif find_analysis < 0 < find_dialing:
            r["analysis"] = f[find_dialing + 4:].replace("\n", "").replace("【点拨】", "")
        else:
            r["analysis"] = "无解析"
        # print(r["analysis"])

        if len(r["answer"].split(",")) > 1:
            multiple_question.append(r)
        else:
            choice_question.append(r)
    # 返回结果
    return [{"type": 1, "data": choice_question}, {"type": 2, "data": multiple_question}]
