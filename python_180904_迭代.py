
# 迭代
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历我们称为迭代（Iteration）。


############################
# list
L = list(range(10))
for value in L:
	print('L-value:', value)
	
# Python内置的enumerate函数可以把一个list变成索引-元素对
for index, value in enumerate(['a', 'b', 'c', 'd']):
	print('index: %d, value: %s' % (index, value))
	
for x, y in [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]:
	print('x: %d, y: %s' % (x, y))
	
	
############################
# tuple （同list）
for index, value in enumerate(('A', 'B', 'C', 'D')):
	print(index, '--', value)
	
	
############################
# dict
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 默认迭代的是Key
for key in d:
	print('key:', key)
	
for value in d.values():
	print('value:', value)

for key, value in d.items():
	print('key: {0}, value:{1}'.format(key, value))	
for t in d.items():
	print(t)
	
	
############################
# string

for c in 'abcdefg':
	print('string -- c:', c)


############################
# 如何判断一个对象是可迭代对象呢？
# 方法是通过collections模块的Iterable类型判断

from collections import Iterable

print(isinstance('abc', Iterable))

print(isinstance(123, Iterable))


	

