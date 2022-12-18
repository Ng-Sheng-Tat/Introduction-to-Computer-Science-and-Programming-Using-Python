### Unit 1 Notes

**What does a computer do?**
- it performs *calculations* at extremely high speed
    - arithmetic calculations (primitive)
    - logical calculations
    - but we need good algorithms to get the computation fast enough
- it remembers *results* on the storage disks
- there is limit to computations nowadays

**Types of knowledge** that users can pass to the computer to instruct it to do something
1. *Declarative Knowledge* is a statement of fact to a solution
2. *Imperative Knowledge* is a recipe or *how-to* computation to a solution
    - consists of sequence of simple steps, flow of control process that specifies when each step is executed, a means of determining when to stop

**Types of Machines in Computer**
1. Fixed program
    - like a calculator
2. Stored program computer
    - consists of machine that stores and executes instructions
    - there are a sequence of *instructions* stored inside the computer which built from predefined set of primitive instructions like arithmetic and logic, simple tests, and moving data
    - consists of special program (interpreter) that executes each instruction in order which is used to tests to change flow of control through sequence and stop when done
    - one can compute anything with only 6 primitives, which are move left, move right, scan, read, write, and do nothing (modern programming languages might have more)
    - abstract methods can be used to create new primitives
    - computer science property known as turing complete, which states that if you can do one thing with one programming language, you can do the same thing with other programming languages

**Basic Machine Architecture**
<figure>
    <center>
    <img src = "Basic Machine Architecture.png" alt = "Basic Machine Architecture">
    <figcaption>Basic Machine Architecture</figcaption>
</figure>

**Creating Recipes**
- a programming languages provides a set of primitive operations
- expressions are complex but legal combinations of primitives in a programming language
- expressions and computations have values and meanings in a programming language
- primitive constructs for programming languages are numbers, string, simple operators
- languages have both syntax (grammar) and static or not static semantics (meaning) 

**Objects**
- programs manipulate data objects
- each object have *types*, which can be either scalar or non-scalar
- *Scalar Objects*, int, float, bool, NoneType (None), which can be checked using ``type()`` command
- *Casting* for converting the data type, by using command like ``float(5)``
- ``print()`` command to the console, its return is ``None`` (NoneType)

**Expressions**
- it combine objects and operators to form expressions
- Syntax '<object> <operator> <object>'

**Floating Point Error**
Decimal numbers cannot be stored exactly in the computer because the computer does not have an infinite amount of memory. So decimal numbers are rounded when stored. When you do calculations with these numbers, your final result will be different than the actual result. For example, you may get something like 5.0000000044 instead of 5.0.

**Variables**
- supports code reuse
- the code is executed sequentially

**Short Hand Swapping**
```
a = 1
b = 2
a, b = b, a
```
