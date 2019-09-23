
info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

print(info['name'])
print(info['address'])
print("======若访问不存在的键，则会报错：-------")
print("在我们不确定字典中是否存在某个键而又想获取其值时，可以使用get方法，还可以设置默认值：")
age = info.get('age')
print(age)
print(type(age))
age = info.get('age', 18) # 若info中不存在'age'这个键，就返回默认值18
print(age)


print('删除前,%s'%info['name'])
del info['name']
# print('删除后,%s'%info['name'])

print("del删除整个字典")
del info

print("clear清空整个字典")
# info.clear()

# len() 测量字典中，键值对的个数
dict = {"name":"zhangsan","sex":"m"}
print(len(dict))

# keys
print(dict.keys())
# values
print(dict.values())
# items 返回一个包含所有（键，值）元祖的列表
print(dict.items())
dict2 = dict.items()

# has_key dict.has_key(key)如果key在字典中，返回True，否则返回False
# Python3 字典 has_key() 被移除使用 in代替
print('name' in dict)

# 遍历
for key, value in dict.items():
    print("key=%s,value=%s" %(key,value))

# 带下标索引的遍历
chars = ['a', 'b', 'c', 'd']
i = 0
for chr in chars:
    print("%d %s" %(i, chr))
    i += 1

# enumerate()
for i, chr in enumerate(chars):
    print(i, chr)