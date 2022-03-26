import re

old_text = 'MOCK_DATA.txt'
new_text1 = 'file1.txt'
file_read = open(old_text,mode ='r',encoding='Latin1')
file_write1 = open(new_text1,mode ='w')
class_text1 = file_read.read()
seacher1 = r"[A-Z]+[a-z]+\s"

result1 = re.findall(seacher1,class_text1)
for i in result1:
    print (i)
    file_write1=(i+'\n')

