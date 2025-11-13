What is Python's main characteristic regarding syntax compared to other programming languages?
- writing: syntax no ;(semicolon) and {}(curly braces), indentation matters
           variables dynamically typed
- compile and run: interpreter to execute the code and directly gets compiled into machine code
                   automatic garbage collection
- community and supports: simple to learn and write, more Data/ML modules,packages, libraries

What are the basic data types available in Python?
- numeric: int, float, complex
- text: str
- boolean: bool
- multiples: list, tuple, set, dict
- others: bytes, bytearray, memoryview, NoneType
* mixing data type, you get TypeError

Why is indentation important in Python?
- writing: it's a syntax requirement, it defindes code block
           readability, consistency, reduce ambiguilty
- if not follow, we'll get IndentationError or TabError

What happens when you try to mix incompatible data types in an operation?
- TypeError

What is Git Flow?
- it's a branching model
- helps manage development and release cycle
- branches: main (<->hotfix) <- release <- develop (<-> feature)

Operation == vs is 
- checks values <-> checks referencce/memory


Implicit vs explicit type conversion
- automatic by compiler <-> by casting(by programmer)

What's the difference between if x: and if x == True:?
- concept of True-eveluating
- for boolean type the same, for non-boolean type, if x first convert x into it's boolean equivalent
- True: numerics not 0, multiples not empty, not None

Immutable                           vs mutable data types
- int, float, bool, string         <-> list, set, dict
- quick access, cheaper in storage <-> flexible, recommended

List vs tuple
- list advantage: mutable, list-specific operations(ex: append, extend, remove)
- tuple advantage: immutability -> memory efficientcy, iteration speed(sort in concecetive blocks)

List operation:
- list.append(x) for adding one single element at the end
- list.extend([x,x]) adds an intereable at the end
- list.insert(i,x) adds one element to specific index

Shallow copy vs deep copy 
- list.copy(), list[:] <-> copy.deepcopy()
- copies referencing to same object <-> recursively constructs a new compound object and insert a copy of that object into the new compound object

Set comprehensions   vs converting a list comprehension to a set?
- fast, consistence <-> handles complex logics, takes intermediate process, debug

What's the time complexity difference between checking membership (`in` operator) in a list vs a set?
- list: linear, O(N)
- set: hashbased look-up, O(1) -> it's based on a hash table but key is Null

* Why are tuples immutable but you can still modify a list inside a tuple? -> because it's holding a reference
-> means if the elements in a tuple is a mutable object, such as a list, then the contents of that mutable object can be modified
-> The tuple itself still holds the same reference to that list object, but the list object's internal state can be altered because lists are mutable

List slicing:
- my_list[start:end:step]
- ex: my_list = [0,1,2,3,4,5,6,7,8,9]
      my_list[::2]  return [0, 2, 4, 6, 8]
      my_list[::-1] return [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
      my_list[1::3] return [1, 4, 7]

* What's the difference between remove(), `pop()`, and `del` for lists?
List CRUD's U/D
- del is an operation, use as 'del a[1]', supports slicing, can remove by index or the whole list
- remove() and pop() is method, remove() remove the fist matching value found 
- pop() return and remove at the same time

What is a lambda function, and how is it different from a regular function in Python?
- small annomynous function, (may have multiple arguments) only one expression
- syntax: 'lambda arguments : expression'

What is the difference between *args and **kwargs in function definitions?
- argument collectors
- *args -> takes any number of arguments, and made the args into tuple
- **kwargs -> take any number of KEYWORD arguemnts

What is LEGB? Explain LEGB rule with a code example
- They are scope levels, Local, Enclosing, Global, and Built-in, respectively
- Scope of the name defines the region in the program where you can unambiguously acccess the name
- local->body of the function or lambda expression; enclosing -> nested functions; global ->yopmost in an interactive session;
  built-in -> whenever you run a session, like built-in functions, exceptions

What is a closure in Python? How is it different from a regular nested function?
- Closure is a specific type of nested function
- Clouser can access variables that are local to enclosing scopes, and do so when they are executed outside of that scope

What is the purpose of if __name__ == "__main__":?
- provide clear entry point, prevent uninteded execution(like when it's imported as a module)

Can you modify a global variable inside a function without using the global keyword?
- No, if directly assigning, will return UnboundLocalError
- what do -> use global keyword

In what order must you define parameters in a function signature?
- def function_name(positional_only_param, /, positional_or_keyword_param, default_param=default_value, *args, keyword_only_param, **kwargs):

What is the difference between the global and nonlocal keywords?
- global keyword modifies a variable in the global scope (outside all functions)
- while nonlocal keyword modifies a variable in the nearest enclosing non-global scope (an outer function's scope) within nested functions

What is a common pitfall when using mutable default arguments?
- default mutable object (like a list or dictionary) is created only once when the function is defined, and then it is shared and mutated across all subsequent calls that use the default
- this leads to unexpected behavior where changes made during one function call persist into the next, and can be hard to debug. 
- what do? use None

What is a higher-order function? Give examples of built-in higher-order functions
- either 1. takes another function as an argument or 2. returns a function as a result
- common built-in ones: map(), filter(), sorted()


### **1. Four Principles of OOP**

1. **Encapsulation** – Bundling data (attributes) and methods (functions) that operate on that data into a single unit (class). It hides internal details from external access.
2. **Abstraction** – Exposing only essential features while hiding the complex implementation details.
3. **Inheritance** – Creating new classes from existing ones to reuse and extend functionality.
4. **Polymorphism** – Allowing different objects to be treated through the same interface, where the same method behaves differently depending on the object.

---

### **2. `__str__` vs `__repr__`**

* **`__str__`** → Returns a *user-friendly* string representation of an object, meant for readability (`str(obj)` or `print(obj)`).
* **`__repr__`** → Returns a *developer-friendly* representation of an object, ideally one that can recreate the object (`repr(obj)` or in the REPL).

**Example:**

```python
class Person:
    def __str__(self):
        return "Person object"
    def __repr__(self):
        return "Person(name='John', age=30)"
```

---

### **3. Magic Methods like `__eq__`**

Magic methods (dunder methods) define how built-in operators work for custom objects.

* **`__eq__`** defines equality (`==`).
* **`__lt__`**, `__gt__`, etc., define comparisons.

**Example:**

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

Now, `Point(1,2) == Point(1,2)` returns `True`.

---

### **4. `@classmethod` vs `@staticmethod`**

* **`@classmethod`**

  * Takes `cls` as the first parameter.
  * Can access/modify *class-level* attributes.
  * Used for alternative constructors.

  ```python
  class Circle:
      def __init__(self, radius):
          self.radius = radius
      @classmethod
      def from_diameter(cls, diameter):
          return cls(diameter / 2)
  ```
* **`@staticmethod`**

  * Takes no `self` or `cls`.
  * A utility function logically related to the class but doesn’t access class or instance data.

---

### **5. Property Decorators**

Property decorators (`@property`) let you use methods like attributes while keeping encapsulation.
They’re used to control access, validation, or computed values.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
```

---

### **6. Public, Protected, Private Attributes**

* **Public (`var`)** → Accessible anywhere.
* **Protected (`_var`)** → Conventionally internal use (not enforced).
* **Private (`__var`)** → Name-mangled to prevent accidental access (`_ClassName__var`).

---

### **7. Singleton Pattern**

Ensures only one instance of a class exists.

**Implementation:**

```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

### **8. Factory Pattern**

Creates objects without specifying the exact class of the object to be created.

**Example:**

```python
class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
```

Used when object creation logic is complex or dynamic.

---

### **9. `self` Parameter**

Refers to the current instance of the class.
It allows access to instance attributes and methods.

```python
class Dog:
    def bark(self):
        print(f"{self} is barking!")
```

---

### **10. Abstract Base Classes (ABC)**

Used to define interfaces that derived classes must implement.
Defined in `abc` module.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"
```

You can’t instantiate `Animal` directly — only subclasses that implement `speak()`.


## ✅ **What is a decorator in Python, and where is it used?**

A **decorator** is a function that takes another function as input, adds functionality to it, and returns a new function—without modifying the original function's code.

**Used for:**

* Logging
* Authentication / authorization
* Caching
* Performance measurement
* Input/output validation

Example:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet():
    print("Hello")
```

---

## ✅ **Difference between a generator and a function that returns a list**

### **Generator**

* Uses `yield`
* Produces values one at a time (lazy evaluation)
* Doesn’t store all values in memory
* Returns an *iterator*

### **Function returning a list**

* Computes all values upfront
* Stores entire list in memory
* Potentially expensive for large outputs

---

## ✅ **When choose generators over lists? Memory implications**

Choose **generators** when:

* Dataset is large or infinite
* You want lazy evaluation
* You want faster start time (first item available instantly)

**Memory implications:**

* **List**: O(n) memory (stores everything)
* **Generator**: O(1) memory (stores only the current value)

---

## ✅ **Threading vs Multiprocessing vs Asyncio**

### **Threading**

* Multiple threads inside one process
* Good for **I/O-bound** tasks
* Limited by the **GIL**
* Not ideal for CPU-heavy tasks

### **Multiprocessing**

* Multiple processes, each with its **own Python interpreter**
* Bypasses the GIL
* Good for **CPU-bound** tasks
* Higher memory usage (each process has its own memory)

### **Asyncio**

* Single-threaded concurrency using an event loop
* Cooperative multitasking
* Excellent for **high-volume I/O** (network calls, database calls)
* Not useful for CPU-heavy tasks without moving to threads/processes

---

## ✅ **What is the GIL? How does it affect threading and multiprocessing?**

**GIL = Global Interpreter Lock**, a mutex that allows only **one thread** to execute Python bytecode at a time.

### **Effects**

* **Threading**

  * Threads cannot run CPU-bound Python code in parallel
  * Good for I/O tasks because GIL is released during I/O waits

* **Multiprocessing**

  * Each process has its own interpreter → **no shared GIL**
  * True parallelism for CPU-bound tasks

---

## ✅ **When to use threading, asyncio, and multiprocessing?**

### **Use Threading when:**

* Tasks are **I/O-bound**
* Examples:

  * Web scraping
  * File operations
  * API calls

### **Use Asyncio when:**

* High concurrency of I/O tasks
* You want lightweight coroutines instead of threads
* Examples:

  * Async web servers
  * Managing thousands of network connections

### **Use Multiprocessing when:**

* Tasks are **CPU-bound**
* Examples:

  * Machine learning computations
  * Video/image processing
  * Data transformations

---

## ✅ **CPU-bound vs I/O-bound tasks**

### **CPU-bound**

* Heavy computation
* Performance limited by CPU speed
* Examples: number crunching, image processing

### **I/O-bound**

* Waiting on external resources (network, disk, DB)
* CPU spends most time idle
* Examples: reading files, API calls, DB queries

---

## ✅ **Difference between `yield` and `return`**

### `return`

* Ends the function and returns a value
* Function cannot continue execution afterward

### `yield`

* Pauses the function and returns a value
* Function retains its state
* Can resume execution on next iteration

---

## ✅ **Difference between using `open()` with explicit `.close()` vs using `with`**

### Explicit open/close:

```python
f = open("file.txt")
data = f.read()
f.close()
```

**Risks:**

* If an exception occurs, `close()` may never be called
* Can cause resource leaks

### Using `with`

```python
with open("file.txt") as f:
    data = f.read()
```

**Benefits:**

* Automatically closes file
* Safe even if exceptions occur
* Cleaner and more Pythonic

---

## ✅ **How to handle exceptions? Why is it important?**

### Handling exceptions:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup code")
```

### Why it's important:

* Prevents program crashes
* Allows graceful recovery
* Helps communicate errors clearly
* Enables logging and debugging
* Ensures cleanup of resources (e.g., DB connections, files)



