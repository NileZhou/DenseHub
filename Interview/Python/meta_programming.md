# operate module in runtime

load a module in runtime (because we don't know the spec module when write code, only in runtime we can know spec module path):

```python
from importlib import import_module

module = importlib.import_module('<module_path>')
```


get static code of a module:

```python
import inspect

module = inspect.getmodule(target_obj)
module.__file__
```

# compile code to code object

```python
code = compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
```

- source: could be a string, bytes, or AST object.
- filename: name of code file, if not from file, pass a recognizable value (usually ''). When source is passed, filename is empty.   
- mode: specify the type of compiled code. When source contains a series of statements (e.g., for loop statement), use exec mode. When source is composed of a single expression, use eval mode. When source is composed of a single interactive statement (e.g., input), use single mode.


# exec code in runtime

builtin exec()

```python
# code: str or code object
# globals: dict, used to store global variables
# locals: dict, used to store local variables
exec(code, globals, locals)
```

example:
```python
>>> age = 10
>>> exec('abc = age + 1')
>>> exec('abc = age + 1', {})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'age' is not defined

# input a dict, it will be used as globals, and new result will be written to it
>>> exec('abc = age + 1', {'age': 2})
>>> d = {'age': 2}
>>> exec('abc = age + 1', d)
>>> d['abc'], d['age']
(3, 2)
```


