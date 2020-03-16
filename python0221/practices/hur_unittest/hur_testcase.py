# 写一个测试类，对我们的MathMethod模块里面的类进行单元测试


import unittest
from python0221.practices.hur_unittest.MathMethod import MathMethod  #导入测试目标类
class TestMathMethod(unittest.TestCase):  #继承了unittest中TestCase类，专门用来写测试用例
# 编写测试用例注意：1.一个测试用例就是一个函数，且函数不能传参，只有self参数
# 2.所有的用例（函数）必须以 test 开头，否之执行用例时不能识别
# 用例：1+1
    def test_add_two_positive(self):
        res=MathMethod(1,1).add() #类必须创建实例才能调用函数、方法、属性等
        print(res)
# 用例：5-1
    def test_sub_two_num(self):
        res=MathMethod(5,1).sub()
        print(str(res))

if __name__ == '__main__':
        # TestMathMethod.test_add_two_positive()#在函数文件内可通过调用函数的方法调用
        TestMathMethod("test_add_two_positive") #也可以通过创建实例调用。但是在模块外必须通过实例来调用函数,实例调用函数看类或父类是否有初始化函数
        # unittest.main() #执行所有按照ASCII编码排序  点：执行通过，执行通过3条就有3个点   1：代码出错   F：执行失败