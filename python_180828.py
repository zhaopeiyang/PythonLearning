# print absolute value of an integer:
a = 100
if a >= 0:
	print(a)
else:
	print(-a)
	
# 1. 采用缩进方式。
# 2. 当语句以冒号:结尾时，缩进的语句视为代码块。
# 3. Python程序是大小写敏感的。


################################

# 数据类型：
# 1. 整数
# 2. 浮点数 1.23x10^9就是1.23e9, 或者12.3e8
# 	整数和浮点数在计算机内部存储的方式是不同的，
# 	整数运算永远是精确的（除法难道也是精确的？是的！），
# 	而浮点数运算则可能会有四舍五入的误差。
# 3. 字符串：以单引号'或双引号"括起来的任意文本
print('''line1
line2
line3
line4''')


print(r'''hello,\n
world''')

# 4. 布尔值：True、False
#	布尔值可以用and、or和not运算。(与、或、非)
# 5. 空值： None

################################

# 变量：
#	变量名必须是大小写英文、数字和_的组合，且不能用数字开头
#	同一个变量可以反复赋值，而且可以是不同类型的变量

n = 123		# n是整数
print(n)

n = 'abc'	# n变为字符串
print(n)

################################

# 常量：
# 所谓常量就是不能变的变量，
# 比如常用的数学常数π就是一个常量。
# 在Python中，通常用全部大写的变量名表示常量

PI = 3.1415926
# 但事实上PI仍然是一个变量，
# Python根本没有任何机制保证PI不会被改变，
# 所以，用全部大写的变量名表示常量只是一个习惯上的用法，
# 如果你一定要改变变量PI的值，也没人能拦住你。

# 除法：
# 在Python中，有两种除法，一种除法是/，
#	/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数
#	//除法只取结果的整数部分
# 余数运算 %（取余）


# 练习：
print('\n练习：\n')

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print('n =', n)
print('f =', f)
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)
print('s4 =', s4)


