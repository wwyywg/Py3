from operator import eq, le, ne, ge, gt

# 运算符
print("hello"+"itcast") # 字符串、列表、元组
print([1,2]+[3,4])  # 字符串、列表、元组
print(('a','b')+('c','d'))  # 字符串、列表、元组
print(3 in [1, 2])  # 字符串、列表、元组、字典
print(4 in (1, 2, 3, 4))    # 字符串、列表、元组、字典

# cmp 注意：cmp在比较字典数据时，先比较键，再比较值。
# python 3.4.3 的版本中已经没有cmp函数，被operator模块代替，在交互模式下使用时，需要导入模块。
print(eq({"a":1}, {"b":1}))

print(len("hello itcast"))
print(max("hello itcast"))

print(max({"a":10, "b":2}))

# del del有两种用法，一种是del加空格，另一种是del()
a = 1
del a

b = 2
del(b)

tuple1 = [(2,3),(4,5)]
tuple2 = tuple1+[(3)]
print(tuple2)

a = 1
b = a
print(b)

a = 2
print(b)

a = [1, 2]
b = a
print(b)

a.append(3)

print(b)









