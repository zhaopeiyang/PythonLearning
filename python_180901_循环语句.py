# python中有两种循环语句：
# 1. for...in
# 2. while

# 另外 
# break可以跳出循环语句；
# continue可跳出本次循环，进入下一次循环

#########################################
# 1. for...in
l = ['fsf', 1332, True, 'gse', 'hgksh']
for str in l:
	print(str)
	

for number in list(range(10)):
	print(number) # 打印 0到9
print('-----End-----')
	
for number in list(range(3, 10)):
	print(number)
print('-----End-----')
	
# list() 将range转为列表
# range(5) 意思是起点为0，终点小于5
# range(3, 10) 起点是3，终点小于10


for x in range(4, 9):
	print(x) # 打印 4到8
print('-----End-----')


##########################################
# 2. while

a = 0
while a < 10:
	print(a)
	a += 1










