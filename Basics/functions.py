#Function
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))


def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)


def func():
    print("case 1")
    return 200
x=func()
print(x)


 def func(a,b):
     print("a:"a)
     print("b:",b)
     return
     
  def varableArgs(*a):
      print("list:",a)
      return
    variableArgs(10,20)
    variableArgs(10,20,30,40)
    variableArgs(10,20,'python')   
    func(10,20)

#lambs
x = lambda a: a + 10
print(x(5))

