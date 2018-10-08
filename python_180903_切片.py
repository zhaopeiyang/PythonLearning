
# 
# [a:b:c]
# 切片是生成新的list、tuple或str
# 从第a位元素开始，到b位元素之前（即b-1位），每c个元素取一个
# 例如：L = [0, 1, 2, 3, 4, 5, 6]
# L[1:5:2] = [1, 3]
# 当a=0、c=1时，可省略; 倒数切片取到最后时，b省略
# 当a、b、c全部省略时，相当于复制功能

L = ['afds', 'ege', 'xgr', 'h5w', 'ljui', 'ned']

print('L[0:3] =', L[0:3])
print('L[1:5] =', L[1:5])
print('L[:4] =', L[:4])

# Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print('L[-3:-1] =', L[-3:-1])
print('L[-3:] =', L[-3:])

print('L[:5:2] =', L[:5:2])

# 只写[:]就可以原样复制一个list
print('L[:] =', L[:])

L = list(range(10))
print('list(range(10)) =', L)

T = tuple(range(10))
print('tuple(range(10)) =', T)

