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

OOP principles:
1. Abstraction: exposing only essential features while hiding implementation details
2. Encapsulation: wrapping data or methods into a single class
3. Inheritance: we have subclass from superclass, and we can extend the superclass to reuse its functionality
4. Polymorphism: allowing different objects to be treated throught the same interface, by overriding and overloading

What's the difference between __str__ and __repr__ magic methods?
* magic methods are method starting and ending in __, built-in class in python
      __str__ defines the behaviour when str() is called -> user-friendly
  and __repr__ return a machine readable representation of a type -> developer friendly
  
How do magic methods like __eq__ affect object comparison?
* Magic methods (dunder methods) define how built-in operators work for custom objects.
- used in == compareison, check value based equality
  
Explain the difference between @classmethod and @staticmethod
classmethod -> bound to a class
staticmethod -> behaive like a regular method

What are property decorators in Python?
* decorators are wrappers in a function, it's a callable that returns callable
 - use as @property
 - can have getters, setters, deleters

What's the difference between public, protected (_), and private (__) attributes?
* they are access modifier
 - public: anywhere in the program
 - when a method starts with _, this is for convention only, if you directly call it, you can still access it
 - private -> python does not enforce strict restrictions, you should use Name Mangling, but direct access from outside will raise AttributeError

What's Singleton pattern? How to implement it?
- Ensures only one instance of a class exists.
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

What's Factory pattern? How to implement it?
- Creates objects without specifying the exact class of the object to be created.
- Used when object creation logic is complex or dynamic.

class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
  
What is the self parameter?
- Refers to the current instance of the class. It allows access to instance attributes and methods.

What are abstract base classes (ABC) in Python?
- Used to define interfaces that derived classes must implement.
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

What is a decorator in Python, and where is it used?
- Decorator is use when you want to wrap a function as a function, you can take a function as input, add functionality and return a function
- use for logging, log-in, caching, performance check, I/O validation
  
What's the difference between a generator and a regular function that returns a list?
Generator
* Uses `yield`
* Produces values one at a time (lazy evaluation)
* Doesn’t store all values in memory
* Returns an iterator

Function returning a list
* Computes all values upfront
* Stores entire list in memory
* Potentially expensive for large outputs

  
When would you choose generators over lists, and what are the memory implications?
you chose generator when you want lazy evaluation and save some memory bc generator uses O(1) memory and list use O(n)

Explain the difference between threading, multiprocessing, and asyncio in Python

What is the Global Interpreter Lock (GIL)? How does it affect threading and multiprocessing?

When to use threading, asyncio, multiprocess?
What are CPU-bound vs IO-bound tasks?

What's the difference between yield and return in a function
`yield`: pause and return a value, function retains it state and you can resume later
`return` just return and it's done

What's the difference between using open() with explicit close() vs using the with statement
- open/close: if an exception occur, it may never close -> resource leak

```python
f = open("file.txt")
data = f.read()
f.close()
```

- Using `with`: automticaly close the file, safer whrn there's exception

```python
with open("file.txt") as f:
    data = f.read()
```



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

How to handle exceptions? Why is it important?
 - Exception handling: use try-except-finally block
 - prevent program crash and helps communicate erors

What are primary keys and foreign keys? How are they used in relational databases?
- primary key is unique in the table and can not be null, foreign key is use for provid

What is the difference between INNER JOIN, LEFT JOIN, and FULL OUTER JOIN?
- Inner join: resulf with matching values
- Left join: everything from left table + matching from right table
- Full join: match from either tables
  
What is normalization?
- A process to reduce anomilies, so we have better consistency/simplufy/standerization
- 1NF ->single value attribute
- 2NF -> all non-primary key is depend on primary key
- 3NF -> Transitive Dependency
  
What are the different types of database relationships (1:1, 1:many, many:many) and how do you implement them in SQL?
- 1-1 : one record can be link to exactly one record in another table -> foreign key in the table is also unique in that table
- 1-many: 1 record can be link to many records in another table -> foreign key in the "many" side reference to the primary key to "1" side
- many-many: many records link to many records -> need a intermediate/junction table

What are transactions and isolation levels? Explain the problems each isolation level solves.
1. Read uncommited: lowest level, can see changes made by other transactions -> cause dirty read, non repratable reads, phantom reads
2. Read committed -> only see changes by other committed reads, solves dirty read
3. Repeatable reads -> gurantee transaction will see same data throughtout its duration, eliminates non-repeatable read
4. Serializeable -> highest level, all transactions executed sequentially, no phantom reads


What's the difference between PRIMARY KEY, UNIQUE, and FOREIGN KEY constraints?

