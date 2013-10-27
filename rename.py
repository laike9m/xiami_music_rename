import os
import re

file_list = os.listdir()
aim_file_types = ['.mp3', '.MP3', ]

for ori_name in file_list:
    new_name = ori_name.split(' - ')[-1]
    repeat = 0
    temp_name = new_name
    filename, extended_name = os.path.splitext(new_name)

    if extended_name in aim_file_types:
	
        # 解决重命名后文件同名问题
        while os.path.exists(temp_name):
            temp_name = new_name
            repeat += 1
          
            # 重命名为形如song_1.mp3, 无视非音乐类型
            temp_name = filename + '_%s' % repeat + extended_name 
        else:
            if not repeat:
                # 没有重复文件名
                pass
            else:
                # 有重复文件名
                new_name = temp_name
        os.rename(ori_name,new_name)
        print(ori_name+' completed')
