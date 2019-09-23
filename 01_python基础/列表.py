namesList = ['xiaoWang','xiaoZhang','xiaoHua']
print(namesList[0])
print(namesList[1])
print(namesList[2])

for name in namesList:
        print(name)

length = len(namesList)
i = 0
while i<length:
    print(namesList[i])
    i+=1

# 添加元素("增"append, extend, insert)

#定义变量A，默认有3个元素
A = ['xiaoWang','xiaoZhang','xiaoHua']

# append 通过append可以向列表添加元素
# print("-----添加之前，列表A的数据-----")
# for tempName in A:
#     print(tempName)
#
# #提示、并添加元素
# temp = input('请输入要添加的学生姓名:')
# A.append(temp)
#
# print("-----添加之后，列表A的数据-----")
# for tempName in A:
#     print(tempName)


# extend 通过extend可以将另一个集合中的元素逐一添加到列表中
a = [1, 2]
b = [3, 4]
a.append(b)
print(a)

a.extend(b)
print(a)

# insert insert(index, object) 在指定位置index前插入元素object
a = [0, 1, 2]
a.insert(1, 3)
print(a)

# 查找元素("查"in, not in, index, count)
#待查找的列表
# nameList = ['xiaoWang','xiaoZhang','xiaoHua']
# #获取用户要查找的名字
# findName = input('请输入要查找的姓名:')
#
# #查找是否存在
# if findName in nameList:
#     print('在字典中找到了相同的名字')
# else:
#     print('没有找到')

# index count
a = ['a', 'b', 'c', 'a', 'b']
print(a.index('a', 1, 4)) # 注意是左闭右开区间

print(a.count('b'))
print(a.count('d'))

# 删除元素("删"del, pop, remove)
# del：根据下标进行删除
# pop：删除最后一个元素
# remove：根据元素的值进行删除
movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
print('------删除之前------')


# 排序(sort, reverse)
a = [1, 4, 2, 3]
print(a)
a.reverse()
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)










