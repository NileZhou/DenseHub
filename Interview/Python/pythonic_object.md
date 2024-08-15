- [Private and &#34;Protected&#34; Attributes in Python](#private-and-protected-attributes-in-python)
- [abstract](#abstract)

# Private and "Protected" Attributes in Python

- public member
  can be accessed from the outside of class or module
- private member
  _<var_name>, eg: _internal. It's an agreement, not restricted.

  It can be accessed from outsode
- compulsory private member
  __<var_name>, it will trigger the name mangling, which means the interpreter modify the name of vars
  chaning it to _<Class_name>__<var_name>
- magic member
  like __init__(), __str__() etc.

# abstract

```python
from abc import ABCMeta, abstractmethod

class DemoClass(metaclss=ABCMeta):

    @abstractmethod
    def demo_method(self) -> bool:
        pass
```

We can't instantiate the class directly, it muse be inherited, and all its abstract methods must be implemented in a subclass.


# Module

A module in Python is **a single file** containing Python definitions and statements.

The file name is the module name with the suffix `.py` added. 

For example, a file named `example.py` is a module named `example`.

The module creates **its namespace**, which scopes the functionality it defines. Variables, functions, and classes defined in a module are accessible through the module’s namespace once it is imported into another module or script.
