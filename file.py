"""
os文件处理模块
"""

import os

print(os.path.getsize("./myfile")) # 获取文件大小 字节
print(os.listdir("../day03")) # 获取一个目录下所有文件名
print(os.path.exists("./myfile")) # 查看一个文件是否存在
print(os.path.isfile("myfile")) # 查看一个文件是否为普通文件 -  d
os.remove("myfile" ) # 删除文件
