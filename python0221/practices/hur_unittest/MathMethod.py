
class MathMethod:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
       return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mult(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

if __name__=="__main__":
    print(MathMethod(1,1).add())
    print(MathMethod(1,1).sub())
    print(MathMethod(1,1).mult())
    print(MathMethod(1,1).div())




# 继承  class MathMethod_1(Mathmethod)
# 拓展（父类没有的） 重写（父类有的，重新定义）
# 超继承  supper()





















