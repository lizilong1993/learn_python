# 元编程就是关于创建操作源代码(比如修改、生成或包装原来的代码)的函数和类
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attribute = "example"
        return x


class MyClass(metaclass=MyMeta):
    pass


obj = MyClass()
print(obj.attribute)
