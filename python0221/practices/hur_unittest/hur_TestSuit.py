# 需要挑选用例执行，不执行全部用例时，可以使用用例集TestSuit挑选加载用例
# TestCase  这个类的实例是一个个的单独的用例，，在模块外使用时需要创建实例
import unittest
from python0221.practices.hur_unittest.hur_testcase import TestMathMethod
# 方法一：挑选单挑用例
suit=unittest.TestSuite()
suit.addTest(TestMathMethod("test_add_two_positive"))  #通过实例来调用，是否传参需看父类是否有初始化函数，，这里需要传入 ”methodname“即函数/用例名
# 执行用例
runner=unittest.TextTestRunner()
runner.run(suit)


