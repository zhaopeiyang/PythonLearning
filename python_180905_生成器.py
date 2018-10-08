
# generator

# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器

# 要创建一个generator，有很多种方法。

###########################################################################
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
print(L)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(5))
print(g)
# <generator object <genexpr> at 0x1031a2d58>

print('generator 0 ->', next(g))
print('generator 1 ->', next(g))
print('generator 2 ->', next(g))
print('generator 3 ->', next(g))
print('generator 4 ->', next(g))
# print('generator 5 ->', next(g))
# 没有更多的元素时，抛出StopIteration的错误。

# generator也是可迭代对象
g = (x * x for x in range(5))
for n in g:
	print(n)


###########################################################################
# 第二种方法
# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

def fib(num):
	index, a, b = 0, 0, 1
	while index < num:
#		print(b)
		yield b
		a, b = b, a + b
		index += 1
	return 'done'
	
for n in fib(6):
	print(n)


# 用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)

while True:
	try:
		x = next(g)
		print('g :', x)
	except StopIteration as e:
		print('generator return:', e.value)
		break

