# 函数的参数
# 包括：位置参数、默认参数、可变参数、关键字参数和命名关键字参数


##################################
# 位置参数
def power(x):
	return x * x

print(power(4))


##################################
# 默认参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

def power(x, n = 2):
	s = 1
	while n > 0:
		s *= x
		n -= 1
	return s

print(power(2, 3))

def register(name, age = 25, city = 'beijing'):
	print('name: %s, age: %d, city: %s' % (name, age, city))

register('Jack')
register('Jim', 20)
register('Ann', 23, 'tianjin')
register('Rain', city = 'shanghai')


##################################
# 可变参数

def sum(*numbers):
	s = 0
	for n in numbers:
		s += n
	return s

print(sum(1, 2, 3))
print(sum())

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 3, 5]
print(sum(nums[0], nums[1], nums[2]))
print(sum(*nums))

t = (2, 4, 6)
print(sum(*t))


##################################
# 关键字参数

def person(name, age, **kw):
	print('name: {0}, age: {1}, oter: {2}'.format(name, age, kw))
	
person('Lin', 18)
person('Tom', 23, city = 'Beijing')
person('Kobe', 35, country = 'USA', job = 'Basketball Player')

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'gender': 'Male', 'tall': 175}
person('Devin', 28, **extra)


##################################
# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数

# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
	print(name, age, city, job)
	
person('Benny', 24, city = 'Beijing', job = 'Actor')

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 命名关键字参数可以有缺省值，从而简化调用
def person(name, age, *args, city = 'Beijing', job):
	print(name, age, args, city, job)

person('Lili', 23, 34, 25, city = 'Tianjin', job = 'Teacher')


##################################
# 参数组合
# 参数定义的顺序：位置参数 > 默认参数 > 可变参数 > 命名关键字参数 > 关键字参数

# 对于任意函数，都可以通过类似 func(*args, **kw) 的形式调用它，无论它的参数是如何定义的
args = ['Kane', 23, 'HK', 'Female']
kw = {'city': 'NewYork', 'job': 'Designer'}
person(*args, **kw)

# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。




