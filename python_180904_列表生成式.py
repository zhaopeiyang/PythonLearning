##########################################################
L = list(range(1, 11))
print(L)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


##########################################################
# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = [x * x for x in range(1, 11)]
print(L)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


##########################################################
# for循环后面还可以加上if判断
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)
# [4, 16, 36, 64, 100]


##########################################################
# 还可以使用两层循环，可以生成全排列：
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)
# ['AX', 'AY', 'AZ', 
#  'BX', 'BY', 'BZ', 
#  'CX', 'CY', 'CZ']

L = [x + y for x in range(1, 6) for y in range(6, 11)]
print(L)
# [7, 8, 9, 10, 11, 
#  8, 9, 10, 11, 12, 
#  9, 10, 11, 12, 13, 
#  10, 11, 12, 13, 14, 
#  11, 12, 13, 14, 15]


##########################################################
# 列表生成式也可以使用两个变量来生成list
d = {'a': 'A', 'b': 'B', 'c': 'C'}
L = [k + '=' + v for k, v in d.items()]
print(L)
# ['a=A', 'b=B', 'c=C']


##########################################################
# 把一个list中所有的字符串变成小写
l = ['Hello', 'World', 'Hello', 'Python']
L = [s.lower() for s in l]
print(L)
# ['hello', 'world', 'hello', 'python']


l = ['Hello', 'World', 23, 'Hello', 'Python', None]
L = [s.lower() for s in l if isinstance(s, str)]
print(L)


##########################################################
# 扩展，三层循环
L = [x + y + z for x in 'ABC' for y in 'DEF' for z in 'XYZ']
print(L)
# ['ADX', 'ADY', 'ADZ', 
#  'AEX', 'AEY', 'AEZ', 
#  'AFX', 'AFY', 'AFZ', 
#  'BDX', 'BDY', 'BDZ', 
#  'BEX', 'BEY', 'BEZ', 
#  'BFX', 'BFY', 'BFZ', 
#  'CDX', 'CDY', 'CDZ', 
#  'CEX', 'CEY', 'CEZ', 
#  'CFX', 'CFY', 'CFZ']

