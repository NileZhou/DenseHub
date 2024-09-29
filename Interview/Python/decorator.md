

[TOC]

# @contextmanager



用于创建上下文管理器，简化资源管理。上下文管理器通常用于管理资源，例如文件、网络连接等，确保在使用后正确释放资源。

使用 @contextmanager 装饰的函数可以使用 with 语句来调用，确保在代码块执行前后自动处理资源的获取和释放。具体来说，yield 语句前的代码在进入 with 块时执行，而 yield 语句后的代码在退出 with 块时执行。

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering context")
    yield  # 这里是上下文块
    print("Exiting context")

with my_context():
    print("Inside context")
    
# Expectation output:

# Entering context
# Inside context
# Exiting context
```



# @staticmethod

将方法定义为静态方法，不需要访问实例或类的属性。

```python
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method."

# 调用
MyClass.static_method()  # 可以通过类调用
obj = MyClass()
obj.static_method()      # 也可以通过实例调用
```



# @classmethod

将方法定义为类方法，接收类作为第一个参数（通常命名为 cls

```python
class MyClass:
    class_variable = "Class Variable"

    @classmethod
    def class_method(cls):
        return cls.class_variable

# 调用
MyClass.class_method()  # 通过类调用
obj = MyClass()
obj.class_method()      # 也可以通过实例调用
```



使用 @staticmethod 当你**不需要**访问类或实例的属性时。

使用 @classmethod 当你**需要**访问类的属性或方法时。



# @property

将方法转换为属性，允许通过属性访问而不是方法调用。

```python
class MyClass:
    @property
    def my_property(self):
        return "value"
```



# @functools.wraps

用于保留被装饰函数的元数据（如名称和文档字符串），通常与自定义装饰器一起使用。

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```



# @lru_cache

用于缓存函数的返回值，以提高性能，特别是对于递归函数

```python
from functools import lru_cache

@lru_cache(maxsize=128)  # maxsize 是缓存的最大条目数
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
print(fibonacci(10))  # 55 (从缓存中获取)
```



