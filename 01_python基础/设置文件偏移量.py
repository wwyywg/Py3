f = open('test.txt','r')

str = f.read(30)
print("读取的数据是 : ", str)

# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)

# 重新设置位置
f.seek(5, 0)

# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)

f.close()

# 打开一个已经存在的文件
f1 = open("test.txt", "rb")

# 查找当前位置
position = f1.tell()
print("当前文件位置 : ", position)

# 重新设置位置
f1.seek(-3, 2)

# 读取到的数据为：文件最后3个字节数据
str = f1.read()
print("读取的数据是 : ", str)

f1.close()