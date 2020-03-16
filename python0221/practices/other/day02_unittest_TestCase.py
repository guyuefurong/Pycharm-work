import unittest
from python0221.practices.hur_unittest.MathMethod import MathMethod #导入测试目标类,进入文件-模块-类
# 写一个测试类，用于单元测试MathMethod
class TestMathMathod(unittest.TestCase):  #在unittest基础上创建测试用例类，直接继承框架中 TestCast类
    # 创建测试用例  必须一个函数执行一条用例，函数中不能传参数，函数名必须以“test”开头
    # 用例1：执行1+1
    def test_add(self):
        res=MathMethod(1,1).add()
        print("测试结果：",res)



if __name__ == '__main__':
    unittest.main()  #按照ASCII编码先后顺序执行





# 点 代表执行成功，几个用例几个点   1表示代码出错  F表示执行失败
# 报错：TypeError: expected str, bytes or os.PathLike object, not NoneType 状态码 1
# 原因在于文件以unittest 命名，导致同名模块名无法定位

