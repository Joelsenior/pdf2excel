import blockextract 
import contentextract
path = r'word2excel\\aimed_data\\text.txt'
contentextract.extract_content(blockextract.extract_block(path))