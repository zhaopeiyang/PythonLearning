
# 在Python中，定义一个函数要使用def语句，
# 依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，
# 函数的返回值用return语句返回。

def my_abs(x):
	# 参数类型检查
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
		
	if x >= 0:
		return x
	else:
		return -x
		
print(my_abs(-90))

###########################
# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：

def nop():
	pass

# pass语句什么都不做，那有什么用？
# 实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

def func(x):
	if x > 100:
		pass
		
		
###########################
# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
# 但是如果参数类型不对，Python解释器就无法帮我们检查

# print(my_abs('a'))


##########################
# 返回多个值

import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
	
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# Python的函数返回多值其实就是返回一个tuple
# 在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值

r = move(100, 100, 60, math.pi / 6)
print(r)

	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		