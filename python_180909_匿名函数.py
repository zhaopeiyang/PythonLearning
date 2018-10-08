
r = map(lambda x: x * x, [1, 3, 5, 7, 9])
print(list(r))

# 匿名函数 lambda x: x * x 实际上就是：
def func(x):
	return x * x
	
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。

# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突


# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f(8))


# 也可以把匿名函数作为返回值返回，比如：
def build(x, y):
	return lambda: x * x + y * y
	
fl = build(3, 5)
print(fl())