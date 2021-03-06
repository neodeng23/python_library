

int()             #将一个数值或字符串转换成整数，可以指定进制。
float()          #将一个字符串转换成浮点数。
str()            #将指定的对象转换成字符串形式，可以指定编码。
chr()            #将整数转换成该编码对应的字符串（一个字符）。
ord()            #将字符串（一个字符）转换成对应的编码（整数）。

%s              #字符串 (采用str()的显示)
%r              #字符串 (采用repr()的显示)
%c              #单个字符
%b              #二进制整数
%d              #十进制整数
%i              #十进制整数
%o              #八进制整数
%x              #十六进制整数
%e              #指数 (基底写为e)
%E              #指数 (基底写为E)
%f              #浮点数
%F              #浮点数，与上相同
%g              #指数(e)_x0010_或浮点数 (根据显示长度)
%G              #指数(E)或浮点数 (根据显示长度)
####################################################
#列表
print(len(list1))   #计算列表长度(元素个数
list1.remove(3)     # 删除元素
list1.clear()       # 清空列表元素
fruits2 = fruits[1:4]    # 列表切片

for fruit in fruits:         # 循环遍历列表元素
    print(fruit.title(), end=' ')
print()

fruits2 = fruits[1:4]      # 列表切片

#####################################################
#定义集合
'''Python中的集合跟数学上的集合是一致的
python集合的添加有两种常用方法，分别是add和update
集合update方法：是把要传入的元素拆分，做为个体传入到集合中'''
set1 = {1, 2, 3, 3, 3, 2}
set1.add(5)
set2.update([11, 12])

#####################################################
'''字典是另一种可变容器模型，类似于我们生活中使用的字典，它可以存储任意类型对象，
与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开'''
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['狄仁杰'])

class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age