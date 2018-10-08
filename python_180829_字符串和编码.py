# 字符串和编码
# Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

# 字符 ==> 编码 : ord()函数
A = ord('A')
print('"A"的编码:', A)

A = ord('中')
print('"中"的编码:', A)

# 编码 ==> 字符 : chr()
a = chr(66)
print('编码66是字符:', a)

# 如果知道字符的整数编码，还可以用十六进制这么写str：
a = '\u4e2d\u6587'

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
c = 'ABC'.encode('ascii')
print(c)

c = '中文'.encode('utf-8')
print(c)

# 把bytes变为str，就需要用decode()方法
str = b'ABC'.decode('ascii')
print(str)

str = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(str)

# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
str = b'\xe4\xb8\xad\xee'.decode('utf-8', errors = 'ignore')
print(str)

# 计算str包含多少个字符，可以用len()函数
l = len('abc')
print(l)

l = len('中文')
print(l)

# 如果换成bytes，len()函数就计算字节数
l = len(b'ABC')
print(l)

l = len(b'\xe4\xb8\xad\xe6\x96\x87')
print(l)


################################################

# 格式化

print('hello, %s' % 'world')

print('Hi %s, you have $%d.' % ('Devin', 100000))

print('%2d-%02d' % (3, 1)) # %2d表示有两位，但是十位是空格；%02d表示两位，十位补0

print('%.2f' % 3.1415926)

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('age: %s. gender: %s' % (25, True))

# format()函数
print('Hello {0}, 成绩提示了{1:.1f}%'.format('小明', 17.1234))

# 练习
s1 = 72
s2 = 85
r = (s2 - s1)/s1
print('小明成绩提升了%.1f%%' % r)









