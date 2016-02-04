# encoding: utf-8
# 钻石继承父类被多次初始化是个非常难缠的方法
class Base(object):
    def __init__(self):
        print "Base init"
# # 普通方法
# class Medium1(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print "Medium1 init"
#
# class Mediun2(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print "Medium2 init"
#
# class Leaf(Medium1, Mediun2):
#     def __init__(self):
#         Medium1.__init__(self)
#         Mediun2.__init__(self)
#         print "Leaf init"
# Super方法
class Medium1(Base):
    def __init__(self):
        super(Medium1, self).__init__()
        print "Medium1 init"

class Medium2(Base):
    def __init__(self):
        super(Medium2, self).__init__()
        print "Medium2 init"

class Leaf(Medium1, Medium2):
    def __init__(self):
        super(Leaf, self).__init__()
        print "Leaf init"
leaf = Leaf()
print Leaf.mro()
# [<class '__main__.Leaf'>,
# <class '__main__.Medium1'>,
# <class '__main__.Medium2'>,
# <class '__main__.Base'>,
# <type 'object'>]
# 普通方法
# Base init 第一次调用基类
# Medium1 init
# Base init 第二次调用基类
# Medium2 init
# Leaf init

# super方法
# Base init 只调用一次基类方法
# Medium2 init
# Medium1 init
# Leaf init