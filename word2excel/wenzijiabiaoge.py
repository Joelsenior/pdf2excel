import zipfile
word=zipfile.ZipFile('rawdata.docx') #先压缩
xml=word.read('word/document.xml').decode('utf-8')   #document.xml中有我们需要的文字
# print(xml)
xml_list=xml.split('<w:t>')  #生成的结果是：汉字在，和</w:t>之间
# print(xml_list)  #这里面没有<w:t>，只有</w:t>
text_list=[]
 
for i in xml_list:
    if i.find('</w:t>')+ 1:    #find函数,找到返回第一个位置，否则返回-1
        text_list.append(i[:i.find('</w:t>')])  #找到</w:t>将前面你的汉字加入
    else:
        pass
 
print(text_list)
text="".join(text_list) 
#https://blog.csdn.net/weixin_45786868/article/details/124853289