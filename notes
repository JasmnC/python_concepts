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
- del is an operation, use as 'del a[1]' or 

