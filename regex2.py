"""
re模块函数使用示例
生成match对象的函数
"""
import re

# 目标字符串
s = "Alex:1996,Sunny:1997"
pattern = r"(?P<dog>\w+):(\d+)"

# result 是匹配结果的迭代对象
# result = re.finditer(pattern,s)
# 循环取值
# for i in result:
#     # 取得的是match对象 match--> 获取更丰富的匹配信息
#     print(i.group())  # 获取匹配内容
#     print(i.span())  # 假设(0,9) --> s[0:9] -->就是匹配到的内容


# 匹配第一处符合套件的内容
obj = re.search(pattern,s)
print(obj.group())
print(obj.groupdict()) # 为捕获组生成一个字典 捕获组名字为键，匹配到的对应内容为值

# 匹配字符串开始位置 (相当于自动在正则表达式开始加了一个 ^)
obj = re.match(pattern,s)
print(obj.group('dog'))



