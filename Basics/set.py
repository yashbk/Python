l=[]
type(l)
<class 'list'>
t={}
type(t)
<class 'dict'>
s1={10,}
type(s)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type(s)
NameError: name 's' is not defined. Did you mean: 's1'?
s={10,}
type(s)
<class 'set'>
l=()
type(l)
<class 'tuple'>
t=(t)
type(t)
<class 'dict'>
s={1}
type<class 'dict'>
SyntaxError: invalid syntax
s={l}
x={1,2,3,4}
y={'a','b'}
print(x,y)
{1, 2, 3, 4} {'a', 'b'}
z=x.add(5)
print(x,z)
{1, 2, 3, 4, 5} None
x.clear()
print(x)
set()
y.add('c')
print(y)
{'a', 'c', 'b'}
    x={1,2,3}
    
SyntaxError: unexpected indent
x={1,2,3}
y=x.copy()
print(x,y)
{1, 2, 3} {1, 2, 3}
z=x
print(x,y,z)
{1, 2, 3} {1, 2, 3} {1, 2, 3}
x.add(4)
print(x,y,z)
{1, 2, 3, 4} {1, 2, 3} {1, 2, 3, 4}
print(id(x),id(y),id(z))
2721061130464 2721061131584 2721061130464
#difference
x.difference(y)
{4}
y.difference(x)
set()
print(x=y)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(x=y)
TypeError: 'x' is an invalid keyword argument for print()
print(x-y)
{4}
print(y-x)
set()

x.difference_update(y)




y.difference_update(x)
print(y)
{1, 2, 3}

print(x)
{4}


x={1,2,3,4}
y={1,2,3}
x.difference(y)
{4}
y.difference(x)
set()
print(x)
{1, 2, 3, 4}
x.difference_update(y)
print(x)
{4}

#discard
x.discard(2)
print(x)
{4}
y.discard(2)
print(y)
{1, 3}

#intersection
x={1,2,3,4)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
x={1,2,3,4}
y={1,2,3}
x.intersection(y)
{1, 2, 3}
print(x)
{1, 2, 3, 4}
x.intersection_update(y)
print(x)
{1, 2, 3}

#isdisjoin
x={1,2,3,4}
y={5,6}
x.isdisjoin(y)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    x.isdisjoin(y)
AttributeError: 'set' object has no attribute 'isdisjoin'. Did you mean: 'isdisjoint'?
x.isdisjoint(y)
True
y={1,2}
x.intersection(y)
{1, 2}
x.issuperset(y)
True
y.issuperset(x)
False
y.issubset(x)
True

print(x)
{1, 2, 3, 4}
x.pop()
1
print()

x.pop()
2
x.pop()
3
x={1,2,3,4}
x.discard(3)
print(x)
{1, 2, 4}
x.remove(2)
print(x)
{1, 4}
dir(x)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
print(x)
{1, 4}
x.discard(10)
print(x)
{1, 4}
x.remove(10)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    x.remove(10)
KeyError: 10
print(x)
{1, 4}

#built in function
l=[]
dir(l)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
t=(10,20)
dir(t)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
len(l)
0
all()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    all()
TypeError: all() takes exactly one argument (0 given)
s={1,2,3,4,5,6}
all(s)
True
s={1,2,0,4,5,6}
all(s)
False
#any()
s={1,2,3}
print(all(s))
True
#any() and all()
s={1,2,3}
print(all(s))
True
d={1,0,2}
print(all(s))
True
print(any(s))
True
a={1,2,3,0}
print(any(a))
True
print(all(a))
False

#enumerate()
s={1,2,3,4,5,6}
enumerate(s)
<enumerate object at 0x000002798BD97EC0>
for i in x:
    print(i,end="")

 
14
s={1,2,3,4,5,6}
enumerate(s)
<enumerate object at 0x000002798BE63D00>
for i in s:print(
    print(i,end="")
