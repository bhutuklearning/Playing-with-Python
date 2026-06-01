## Agenda

This file focuses on revising and doing python.
The attempt is to touch the topics and just get my hands dirty again.
Going through the topics again for getting myself ready.

### Info:

To remember that Python is a dynamically typed language, but types are strong.

The Data types to be remembered are:

Numbers: int, float, complex
Text: str
Boolean: bool (True/False)
Sequences: list, tuple, range
Sets: set, frozenset
Mappings: dict
None: NoneType

If I want to print something on the terminal, I don't have to write "\n" to start every statement on the new line, like C language.

More Interesting Stuff (a few picks)

#### Here are a few handy topics to explore next:

Comprehensions: list, dict, set — concise and efficient
d = {i: i*i for i in range(5)}
Context Managers: with open(...) as f: for safe resource handling
Itertools: powerful tools for iteration (cycle, chain, combinations, etc.)
Exceptions: try/except/else/finally to handle errors
Data classes (Python 3.7+): @dataclass for simple classes
Type hints: improve readability and tooling (def f(x: int) -> str:)
Virtual environments: venv to isolate dependencies

#### Important Decorator Concepts
A) Wrapper Function
The wrapper is the extra layer added around original function.

B) Closures
Wrapper remembers the original function even after decorator execution.
This is called closure behavior.

C) Metadata Problem
Decorators can overwrite:
function name
docstring


Example:
```python
print(add.__name__)
```

Might show:
```python
    wrapper
```
instead of:
```python
  add
```

Solution: functools.wraps

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper
```
Always use wraps.

#### Summary of Decorators
a) take a function
b) add extra behavior
c) return modified function