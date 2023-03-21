import xlwt


def write_2_excel(quest_list: list):
    wb = xlwt.Workbook()
    # 添加一个表
    ws = wb.add_sheet('Sheet1')
    # 题型	试题标题	题目	选项A	选项B	选项C	选项D	选项E	选项F	正确答案	解析	对应章节
    ws.write(0, 0, "题型")
    # ws.write(0, 1, "试题标题")
    # ws.write(0, 2, "题目")
    # ws.write(0, 3, "选项A")
    # ws.write(0, 4, "选项B")
    # ws.write(0, 5, "选项C")
    # ws.write(0, 6, "选项D")
    # ws.write(0, 7, "选项E")
    # ws.write(0, 8, "选项F")

    ws.write(0, 1, "题目")
    ws.write(0, 2, "选项A")
    ws.write(0, 3, "选项B")
    ws.write(0, 4, "选项C")
    ws.write(0, 5, "选项D")
    ws.write(0, 6, "选项E")
    ws.write(0, 7, "选项F")
    ws.write(0, 8, "正确答案")
    ws.write(0, 9, "解析")
    ws.write(0, 10, "对应章节")

    q = 0
    for l in quest_list:
        quest = l["data"]

        for row in range(len(quest)):
            ws.write(q + 1, 0, l["type"])
            ws.write(q + 1, 1, quest[row]["stem"])

            quest_array = quest[row]["qest"]

            if len(quest_array) > 0:
                ws.write(q + 1, 2, quest_array[0])
            if len(quest_array) > 1:
                ws.write(q + 1, 3, quest_array[1])
            if len(quest_array) > 2:
                ws.write(q + 1, 4, quest_array[2])
            if len(quest_array) > 3:
                ws.write(q + 1, 5, quest_array[3])

            ws.write(q + 1, 6, "")
            ws.write(q + 1, 7, "")

            ws.write(q + 1, 8, quest[row]["answer"])
            ws.write(q + 1, 9, quest[row]["analysis"])
            ws.write(q + 1, 10, quest[row]["source"])
            q += 1

    wb.save('处理结果0215.xls')
