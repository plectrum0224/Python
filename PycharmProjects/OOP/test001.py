# encoding: utf-8
"""
子类调用父类成员有两种方法，分别为普通方法和Super方法
两种方法如果不涉及多重集成，则结果一样
"""
class Base(object):
    def __init__(self):
        print "Base init"
# 普通方法
# class Leaf(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print "Leaf init"

# Super方法
class Leaf(Base):
    def __init__(self):
        super(Leaf, self).__init__()
        print "Lead init"


leaf = Leaf()
# 结果均为
# Base init
# Lead init