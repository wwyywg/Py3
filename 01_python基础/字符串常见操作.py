mystr = 'hello world itcast and itcastcpp'

# find 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
# mystr.find(str, start=0, end=len(mystr))
print(mystr.find('itcast'))
print(mystr.find("itcast", 0, 10))

# index 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
# mystr.index(str, start=0, end=len(mystr))
print(mystr.index("itcast", 0, 20))

# replace 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
# mystr.replace(str1, str2,  mystr.count(str1))
name = "hello world ha ha"
print(name.replace("ha", "Ha"))
print(name.replace("ha", "Ha", 1))

# split 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
# mystr.split(str=" ", 2)
names = name.split(" ")
print(names)

names2 = name.split(" ", 1)
print(names2)

# capitalize 把字符串的第一个字符大写
# mystr.capitalize()
print(mystr.capitalize())

# title 把字符串的每个单词首字母大写
a = "hello itcast"
print(a.title())

# startswith 检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
# mystr.startswith(obj)
print(mystr.startswith("hello"))
print(mystr.startswith("Hello"))

# endswith 检查字符串是否以obj结束，如果是返回True,否则返回 False.
# mystr.endswith(obj)
print(mystr.endswith("cpp"))
print(mystr.endswith("app"))

# lower 转换 mystr 中所有大写字符为小写
# mystr.lower()
mystr = "HELLO world itcast and itcastcpp"
print(mystr.lower())

# upper 转换 mystr 中的小写字母为大写
# mystr.upper()
print(mystr.upper())

# ljust 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# mystr.ljust(width)
mystr = "hello"
print(mystr.ljust(10))

# rjust 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# mystr.rjust(width)
print(mystr.rjust(10))

# center 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
# mystr.center(width)
mystr = "hello world itcast and itcastcpp"
print(mystr.center(50))

# lstrip 删除 mystr 左边的空白字符
# mystr.lstrip()
mystr = "     hello"
print(mystr.lstrip())
mystr = "     hello     "
print(mystr.lstrip())

# rstrip 删除 mystr 字符串末尾的空白字符
# mystr.rstrip()
mystr = "     hello"
print(mystr.rstrip())
mystr = "     hello     "
print(mystr.rstrip())

# strip 删除mystr字符串两端的空白字符
a = "\n\t itcast \t\n"
print(a.strip())

# rfind 类似于 find()函数，不过是从右边开始查找.
# mystr.rfind(str, start=0, end=len(mystr))
mystr = 'hello world itcast and itcastcpp'
print(mystr.rfind("itcast"))

# rindex 类似于 index()，不过是从右边开始.
# mystr.rindex( str, start=0,end=len(mystr))
mystr.rindex("it")

# partitle 把mystr以str分割成三部分,str前，str和str后
# mystr.partition(str)
print(mystr.partition("itcast"))

# rpartition 类似于 partition()函数,不过是从右边开始.
# mystr.rpartition(str)
print(mystr.rpartition("itcast"))

# splitlines 按照行分隔，返回一个包含各行作为元素的列表
# mystr.splitlines()
mystr = "hello\nworld"
print(mystr.splitlines())

# isalpha 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
# mystr.isalpha()
mystr = 'abc'
print(mystr.isalpha())
mystr = '123'
print(mystr.isalpha())
mystr = 'abc 123'
print(mystr.isalpha())

# isdigit 如果 mystr 只包含数字则返回 True 否则返回 False.
# mystr.isdigit()
mystr = 'abc'
print(mystr.isdigit())
mystr = '123'
print(mystr.isdigit())
mystr = 'abc123'
print(mystr.isdigit())

# isalnum 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
# mystr.isalnum()
mystr = 'abc'
print(mystr.isalnum())
mystr = '123'
print(mystr.isalnum())
mystr = 'abc123'
print(mystr.isalnum())

# isspace 如果 mystr 中只包含空格，则返回 True，否则返回 False.
# mystr.isspace()
mystr = 'abc123'
print(mystr.isspace())
mystr = ''
print(mystr.isspace())
mystr = '  '
print(mystr.isspace())
mystr = '      '
print(mystr.isspace())

# join mystr 中每个字符后面插入str,构造出一个新的字符串
# mystr.join(str)
str = " "
li = ["my", "name", "is", "dingGe"]
print(str.join(li))
str = "_"
print(str.join(li))































