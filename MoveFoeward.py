import functools
import math
from functools import reduce

# 1
# python 高阶 函数式编程, 函数当作函数的参数
from logging import log


def add(x, y, f):
    return f(x) + f(y)


print(add(25, 9, math.sqrt))

# 2
# 高阶函数 map(f , list)   它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
# 3.7中 map（） 的显示问题 需要list( m)转化
print(list(map(math.sqrt, [1, 4, 9, 16, 25])))


# 3
# 高阶函数 reduce( f , list) ，f需要有2个参数 ，f从前两个元素开始计算，结果与下一个元素计算，返回最终结果
# 3.7已经从全局名空间除去，导入才能用   from functools import reduce
def sum(x, y):
    return x + y


print(reduce(sum, [2, 2, 2, 2]))


# 4
# 高阶函数 filter（f , list)，对元素做判断，留下true元素，返回性list
# 需要list( m)转化,
def is_not(s):
    return s and len(s.strip()) > 0


print(list(filter(is_not, ['aaa', ' ', 'bb'])))

# 5
# 高阶函数 sorted( )  对list集合进行排序  字符串按As， sorted( )
# 3.7语法与2.x 不一样
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 6
# 函数返回函数,  f中嵌套g ，并返回g , 把g赋值给 x  调用就会输出g的内容
# 延迟计算
def f():
    print('call f()...')

    def g():
        print('call g()...')

    return g


x = f()
x()


def calc_prod(lst):
    def g():
        def y(a, b):
            return a * b

        return reduce(y, lst)

    return g


f = calc_prod([1, 2, 3, 4])
print(f())


# 7
# 闭包 内嵌函数调用外层函数 便量，外层的返回值为内层函数。
#
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

# 8
# 匿名函数  lambda关键字定义
# 3.7需要强制转化
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 9
# 装饰器 ，最底层函数上 ,装饰一个函数 接收一个函数，用内置函数装饰好底层函数，返回内置函数f返回的底层函数函数, 内置函数与底层函数同参数
#   * args , **kwargs  表示传入任意参数
def f1(x):
    return x * x


def new_f(f):
    def fn(*args, **kwargs):
        print('包装')
        return f(*args, **kwargs)

    return fn


@new_f
def zi():
    return print('底层')


zi()



# 10
# decorator     即注解的使用  ，省去包装指向步骤。
# 带参数的注解 相当于 在外层继续装饰一层
import time

def performance(f):
    def fn(*args, **kwargs):
        t1 = time.time()
        r = f(*args, **kwargs)
        t2 = time.time()
        # print('time is' +str(t2 - t1))
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(factorial(10))

#带参数例子
import time

def performance(unit):
    def perf_decorator(f):
        def new_f3(*args, **kwargs):
            t1 = time.time()
            f(*args, **kwargs)
            t2 = time.time()
            # print('time is' +str(t2 - t1))
            print('带参数计算函数运行时间call %s() in %f  %s ' % (f.__name__, (t2 - t1),unit))
            return f(*args, **kwargs)
        return new_f3
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(factorial(10))


#11
# 装饰器 ，装饰后的函数属性发生变化( name . doc)    ,使用 @functools.xx(f)  注解修饰
def demo1(f):
    def new_demo2(*args, **kwargs):
        print('包装')
        return f(*args, **kwargs)
    return new_demo2

def demo3(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print('call...')
        return f(*args, **kw)
    return wrapper

print('输出函数名'+demo1.__name__)

@demo1
def demo2():
    pass
demo2()
print('装饰后的函数名发生变化'+demo2.__name__)

@demo3
def demo2():
    pass
print('加@function后的函数名发生变化'+demo2.__name__)


#12
#偏函数 ，函数定向参数执行
#functools.partial( function , parameter)  简化
def int2(x):
    return int(x,base=8)

print(int2('12345'))

int3 = functools.partial(int,base=16)
print(int3('12345'))


#13
#导入模块
# import match
#from match import  pow ,  sin , log
#from logging import  log as  logger   //取别名




#14 异常捕获
#cStringIO 和  StringIO 功能相同 效率不同， 从StringIO  c语言编写效率更高
try:
    import  json
except ImportError:
    import  simplejson  as json

print (json.dumps({'python':2.7}))


#15
# 在2.x中加入3.x的规则
# from __future__  import unicode_literals




# FAQ
# s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')
# math.sqrt( x )  开根号
# upper（）字母大写转化  lower(）字母小写转化
# cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# isinstance(t, Person)  函数判断是否是这个类型，返回 true false







