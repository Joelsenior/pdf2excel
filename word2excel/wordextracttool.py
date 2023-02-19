import zipfile
"""如果word中有表格和文字,通过该函数可以将表格和文字都提出，最后输出为字符串,需要import zipfile"""
def docxextract(filename,savename):
    filename = filename + '.docx'
    word=zipfile.ZipFile(filename) #先压缩
    xml=word.read('word/document.xml').decode('utf-8')   #document.xml中有我们需要的文字
    xml_list=xml.split('<w:t>')  #生成的结果是：汉字在 ，和</w:t>之间
    # print(xml_list)  #这里面没有<w:t>，只有</w:t>
    text_list=[]
    for i in xml_list:
        if i.find('</w:t>')+ 1:    #若该列表元素中没有'</w:t>'，则返回-1，通过加1，进入else。
            text_list.append(i[:i.find('</w:t>')]) #文字都是在索引0处，所以切片起始位置缺省。这里i是字符串，用了字符串切片。
            #找到</w:t>将前面你的汉字加入
        else:
            pass
    # print(text_list)
    text="".join(text_list) #join是将列表元素连接起来。
    savename = savename + '.txt'
    with open(savename,'w') as sn:
        sn.write(text)
        print('完成读取word并输出为.txt!')
    # print(text)
    #参考https://blog.csdn.net/weixin_45786868/article/details/124853289
# docxextract('changhenge','谢点提取的')