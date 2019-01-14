# encoding=utf-8
# 随机数，随机读取每一行的数据
import linecache
import random

a = random.randrange(1, 24)  # 1-9中生成随机数
print(a)
# 从文件poem.txt中对读取第a行的数据
theline = linecache.getline(r'menu', a)
print(theline)