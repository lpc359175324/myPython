# 1
# 类创建 与实例化,语法
from operator import lt


class Person(object):
    pass


x1 = Person()

# 2
# 为实例添加属性, 可以做操作。
x1.name = 'aname'
x1.school = 'school'
x1.school = x1.school + 'x'
print(x1.school)

# 3
#  ---3.7 cmp的替代品---
# lt(a, b) 相当于 a < b
# le(a,b) 相当于 a <= b
# eq(a,b) 相当于 a == b
# ne(a,b) 相当于 a != b
# gt(a,b) 相当于 a > b
# ge(a, b)相当于 a>= b
# 排序  sort 排序list 不新建list
# 排序 sorted排序 所有可迭代 新建list
x2 = Person()
x2.name = 'dname'
x3 = Person()
x3.name = 'cname'
L1 = [x1, x2, x3]
L2 = sorted(L1, key=lambda z: z.name)
print(L2[0].name)
print(L2[1].name)
print(L2[2].name)


# 4
# 类的初始化，__init__
# __xxx某个属性以双下划线 开头 ，则不可被外部访问。
# __xxx__ 特殊属性 群可以访问
# _xxx   单下划线, 不应被访问当时可以访问。
# 定义 类属性，所有实例 都可以访问，并且可以动态修改,,  当实例属性与类属性  同名时 ，实例属性优先级 高

class Person2():
    addres = 'beijing'
    count = 0  # 计数实例

    def __init__(self, name, gender, birth, **kwargs):
        Person2.count = Person2.count + 1
        self.name = name
        self.gender = gender
        self.__birth = birth
        for k, v in kwargs.items():
            setattr(self, k, v)


xiaoming = Person2('name', 'ge', 'bir', job='s')

Person2.addres = 'USA'
print(xiaoming.addres)
print(Person2.count)


# 5
# 类中定义函数,
#类中定义，类的绑定方法，用 @classmethod 修饰
class Person3(object):
    s='11'
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        if  self.__score>=80:
                return 'A-优秀'
        if self.__score >= 60:
            return 'B-及格'
        else:
            return 'C-不及格'

p1 = Person3('Bob', 90)
p2 = Person3('Alice', 65)
p3 = Person3('Tim', 48)

print(p1.get_grade())
print(p2.get_grade())
print(p3.get_grade())

#类的继承
#定义 info 类 ，定义student类 ，  定义Teach类
#继承时  要用super初始化父类
class Info(object):
    def __init__(self , name):
        self.name =name


class Student(Info):
    def __init__(self,name,score):
        super(Student , self).__init__(name)
        self.score = score


#多肽
#由子类，向上查找某方法。
#任意对象只要包含某方法，都可以

#type 获取变量信息，类名。
# dir  获取所有属性
#getattr 根据属性名 获取信息
# setattr  根据属性名 设置新得属性
print(type(p1))
print(dir(p1))
print(getattr(p1,'s'))


#定义特殊方法
class Person4(object):
    def __init__(self ,name):
        self.name = name
    def __str__(self):
        return'(Person: %s, %s)'

p6= Person4('555')
print(p6)






