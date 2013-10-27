'''
将文件名为XXX_1_1_1.mp3的文件恢复成XXX.mp3
'''

import os
import re

pattern = re.compile(r'(.*)(_1)+')

file_list = os.listdir()
for name in file_list:
    filename, extend = os.path.splitext(name)
    obj = pattern.search(filename)
    if obj:
        filename = obj.group(1)  #group(0)是整体,从1开始才是真正的括号中的组
        ori_name = name
        name = filename + extend
        os.rename(ori_name, name)
        try:
            print("%s completed" % ori_name)
        except UnicodeEncodeError:
            print("1 file recovery succeed.name can't show.")
