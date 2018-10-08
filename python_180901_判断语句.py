
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>


a = 100
if a > 200:
	print('a大于200，a:', a)
elif a > 100:
	print('a大于100，a:', a)
elif a > 50:
	print('a大于50，a:', a)
else:
	print(a)
	
	
# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数

str = input('输入出生年份:')
birth = int(str)
if birth > 2010:
	print('10后')
elif birth > 2000:
	print('00后')
elif birth > 1990:
	print('90后')
elif birth > 1980:
	print('80后')
else:
	print('大叔')
