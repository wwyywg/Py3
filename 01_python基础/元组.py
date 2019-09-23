
# Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
aTuple = ('et',77,99.9)
print(aTuple)

# 元组的内置函数count, index
# index和count与字符串和列表中的用法相同
a = ('a', 'b', 'c', 'a', 'b')
a.index('a', 1, 3) # 注意是左闭右开区间
print(a.index('a', 1, 4)) # 注意是左闭右开区间
a.count('b')
a.count('d')