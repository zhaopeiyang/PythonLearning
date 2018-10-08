
# dict

# 在Python中，字符串、整数、tuple等都是不可变的，因此，可以放心地作为key；
# 但是tuple中如果含有list,则不能作为key
# 而list是可变的，就不能作为key

d = {'key1': 32, 'key2': 89, 'key3': 78, 100: 'abc'}

d['key4'] = 42
print(d[100])

# 读取时，key不存在会报错
# 判断key是否存在有两种方法
# 一、通过in判断key是否存在
if 'key0' in d:
	print(d['key0'])
else:
	print(d['key1'])
# 二、通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print('key0 is', d.get('key0'))
print('key0 is', d.get('key0', -1))

# 删除用pop
d.pop('key2')

print(d)
print(len(d))

#######################################
# set

# 要创建一个set，需要提供一个list作为输入集合
# 在set中，没有重复的key。

s1 = set([1, 2, 3])
print(s1)

s2 = set([1, 2, 2, 3, 3, 4])
print(s2)

# 添加元素 add(), 重复添加不起作用
s1.add(5)
print(s1)

# 删除元素 remove(), 删除不存在的Key会报错
s1.remove(1)
print(s1)

# 两个set可以做数学意义上的交集、并集等操作
s3 = set([1, 2, 3, 4])
s4 = set([3, 4, 5, 6])
print(s3 & s4)
print(s3 | s4)





