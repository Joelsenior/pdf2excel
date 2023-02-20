import xml.dom.minidom as xdom
xp = xdom.parse('word/document.xml')
root = xp.documentElement
bodys = root.getElementsByTagName("w:body")
body = bodys[0]
for i,ele in enumerate(body.childNodes):
    e_name = ele.nodeName
    print(i,"->",e_name,"is",ele)

