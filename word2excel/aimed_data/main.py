from multiprocessing.connection import wait
import blockextract 
import contentextract
import docxtotxt
path = docxtotxt.docxtotxt('text.docx')
# print(type(path))
path = r'newfilename.txt'
# path = r'text.txt'
contentextract.extract_content(blockextract.extract_block(path))