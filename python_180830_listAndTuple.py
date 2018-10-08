# list 相当于可变数组
# tuple 相当于不可变数组
# 他们内部的元素可以是不同类型的

############################
# list
list = ['adfa', 'fasew', 'gwge']
print('list:', list)

# 长度
length = len(list)
print('The length of list is', length)

firstItem = list[0]
lastItem = list[-1]
print('first item is %s, last item is %s' % (firstItem, lastItem))

# 追加元素
list.append('edc')
print(list)

# 插入元素
list.insert(1, 'second')
print(list)

# 删除末尾的元素
list.pop()
print(list)

# 删除指定的元素
list.pop(1)
print(list)

# 替换指定元素
list[0] = 'first'
print(list)

# 可以有不同类型的元素
list2 = ['string', 123, True]
print(list2)

# 二维数组
list3 = ['adg', 'fsg', ['gwh', 'h3h'], 'lio']
print(list3)
print(list3[2][0])

#############################################

# tuple
tuple = ('whre', 'het', 'hrtr')
print(tuple)

tuple2 = ()
print(tuple2)

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
tuple3 = (1,)
print(tuple3)

tuple4 = ('gew', 'wwe', ['gef', 'cde'])
print(tuple4)

# tuple是不可变的，但内部的list是可变的
tuple4[2].append('adgd')
print(tuple4)















