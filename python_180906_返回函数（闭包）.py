
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

def lazy_sum(*args):
	def sum():
		s = 0
		for n in args:
			s += n
		return s
	return sum


f = lazy_sum(1, 3, 5, 7, 9)

print(f) # <function lazy_sum.<locals>.sum at 0x1039072f0>

print(f()) # 25


#
## 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#
def count():
	l = []
	for i in range(1, 4):
		def f():
			return i * i
		
		l.append(f)
	return l
	
f1, f2, f3 = count()

print(f1()) # 9
print(f2()) # 9
print(f3()) # 9
# 全部都是9！
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

##
# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
	l = []
	def f(j):
		def g():
			return j * j
		return g	
	for i in range(1, 4):
		l.append(f(i))
	return l

f1, f2, f3 = count()
print(f1()) # 1
print(f2()) # 4
print(f3()) # 9


# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
	n = 0
	def counter():
		nonlocal n
		n += 1
		return n
	return counter
	
counterA = createCounter()

print(counterA(), counterA(), counterA(), counterA(), counterA())


counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
	print('测试通过！')
else:
	print('测试失败！')
	
# nonlocal ？？？



