#类和对象

class cl1:
    print("ok")
    pass

'''实例化一个类:
a=cl1()
'''

#构造函数（构造方法）
#self:在类的方法中必须加上self参数
#构造函数：__init__(self,参数)
#构造函数实际意义：初始化
class cl2:
    def __init__(self):
        print("I am cl2 self!")

#给类加参数：给构造方法加上参数
class cl3:
    def __init__(self,name,job):
        print("My name is " +name+ " My job is my "+job)
        
#属性：类里面的变量：self.属性名
class cl4:
    def __init__(self,name,job):
        self.myname=name
        self.myjob=job
        
#方法：类里面的函数：def函数名（self,参数）
class cl5:
    def myfunc1(self,name):
        print("hello!"+name)


class cl6:
    def __init__(self,name):
        self.name=name
      
    def myfunc1(self):
        print("hello!"+self.name)

        

#继承（单继承，多继承）
#父亲类
class father():
    def speak(self):
        print("i can speak!")
#单继承：class 子类（父类）
class son(father):
    pass

#母亲类
class mother():
    def write(self):
        print("i can write!")
        
#多继承
class daughter(father,mother):
    def listen(self):
        print("i can listen")

#重写（重载）(同名-重载)
class son2(father):
    def speak(self):
        print("i can speak2!")
