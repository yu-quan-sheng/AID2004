"""
re模块函数使用示例
"""
import re

# 目标字符串
s = "Alex:1996,Sunny:1997"
pattern = r"(\w+):(\d+)"

l = re.findall(pattern,s) # 正则中有子组的时候，只会获取子组对应的匹配部分
print(l)

# 使用正则表达式匹配到的内容分割字符串，返回分割后内容列表
l = re.split("\W+",s,2)
print(l)

# 使用正则表达式，匹配目标字符串，匹配到的内容用## 替换，返回替换后的字符串
s = re.sub("\W+","##",s,1)
print(s)
