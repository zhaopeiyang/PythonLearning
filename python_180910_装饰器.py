
def now():
	print('2018-09-10')
f = now
f()

print(f.__name__)


# 本质上，decorator就是一个返回函数的高阶函数。
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

# 把@log放到newNow()函数的定义处，相当于执行了语句：
# newNow = log(newNow)
@log
def newNow():
	print('2018-09-11')
	
newNow()


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数.
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
	
# now2 = log('调用')(now2)
@log('调用')
def now2():
	print('2018-09-11 23:21:31')
	
now2()

# 以上两种decorator的定义都没有问题，但还差最后一步。
# 因为我们讲了函数也是对象，它有__name__等属性，
# 但你去看经过decorator装饰之后的函数，
# 它们的__name__已经从原来的'now2'变成了'wrapper'
print(now2.__name__)
	
	
import functools

def log1(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log1
def now3():
	print('2018-09-11 23:32:25')
	
now3()
print(now3.__name__)

	
	
	
	
	
	
	
	
	
	
	
	
	
	