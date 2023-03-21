import xml.dom.minidom as xdom
xp = xdom.parse('word/document.xml')
root = xp.documentElement
bodys = root.getElementsByTagName("w:body")
body = bodys[0]
for i,ele in enumerate(body.childNodes):
    # e_name = ele.nodeName
    # print(i,"->",e_name,"is",ele)
    #找到包含w:t的标签，可能是多个
    wts = ele.getElementsByTagName("w:t")
    ele_text = "" #记录大单元内所有文本
    for wt in wts:   
        ele_text = ele_text + wt.text
    print(ele_text)



