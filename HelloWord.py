print('helloWorld')
# u 前缀字符串 统一编码
print(u'''静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。''')
# 倒序索引 从 -1开始
L = [95.5, 85, 59]

print(L[-1])
print(L[-2])
print(L[-3])
# list 添加到末尾 append()
L.append('李四')
print(L)
# list 添加到指定位置 -1 倒叙第二位
L.insert(0, '张三')
print(L)
# list删除元素  第二次删除时  数组变化 下标不能越界
L.pop(2)
L.pop(3)
print('删除', L)
# list替换
L[0] = 'Bart'
L[-1] = 'Adam'
print(L)
# tuple 元组 不可变化  定义氮元素 元组时整数加 ，
t = (1, 2, 2, 2)
t = (1,)
t = ('A',)
# 元组 内嵌数组 导致元组可变
t = ('a', 'b', ['A', 'B'])
print(t)
# if 判断    if a> 1:      ***        if   not    a<=1 :        ***               if  a>1 :   else  :
# if   a>1:  elif  a>2:
score = 75
if score >= 60:
    print('passed')
# for   in循环
L = [75, 92, 59, 68]
sum = 0.0
for a in L:
    sum = sum + a
print(sum / 4)
# dict， 采用key: value  ,  无序不重复，key不可变 list不能座位key  tuple可以
d = {
    'key1': 1,
    'key2': 2
}
d['Paul'] = 72  # 替换和添加
d.get('key')  # 获取对应值 ，如果没有 返回None
if 'ket' in d:
    print(d['key'])  # if判断是否含有 key
for key in d:
    print(key + '-', d[key])  # 循环遍历 ，数值int与字符串用，链接
print(d)

# set集合  set() 传入一个li1st 无序不重复，in操作符判断集合中是否存在元素  和 循环遍历
A = '2'
L = [1, '2', 3, 3]
s = set(L)
if A in s:
    print('ok')
print('2' in s)
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])  # 循环
for x in s:
    print(x[0] + ':', x[1])
s.add(1)  # 添加 已有 不报错
s.remove(('Adam', 95))  # 删除 没有 会报错  需要判断
if A in s:
    s.remove(A)
print(s)


# 函数 abs()绝对值       str() 转换成string    int()转化为整数第二个参数设置进制
# 自定义函数 返回多个值，是一个元组tuple
def square_of_sum(L):
    sum = 0
    for x in L:
        sum = sum + x * x
    return sum, L


print(square_of_sum([1, 2, 3, 4, 5]))


# 参数赋默认值
def gree(name='word'):
    return print('helllo' + name)


gree('xx')


# 可变参数
def average(*args):
    sum =0
    if len(args) == 0:
        return 0
    for x in args:
        sum = sum + x
    return sum / len(args)
print(average(112,33,5))

# range(1,101)  取范围函数， Slice切片 集合与字符串 ，upper（）字母大写转化  lower(）字母小写转化
L = range(1,101)
print(L[:10])
print(L[::3])
print(L[:50:5])
print(L[-1:5])
print('aBCDEFG'[:1].upper()+'aBCDEFG'[2:])

def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print(firstCharUpper('hello'))

#enumerate() 函数绑定索引
#zip()函数可以把两个 list 变成一个 list
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print (index, '-', name)

print(L.__len__())

#items()  与 iteritems() (不占用额外内存)遍历 dict 的key和 value
#values()  与 itercalues(不占用内存) 遍历迭代 dict的value
#~~

#生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]  能加判断， isinstance 判断对象类型
print ([x*y for x,y in zip (range(1,101,2) , range(2,101,2)) if x  != 0 ])
print('------')

print( [  100*x + 10*y +z   for x in range(1,10)   for  y in range(10)   for z in range(10)  if x==z   ] )









