def multiply(x,y):
    return x*y

op= multiply(1,2)
print(op)

#Multiplication
lop= lambda x,y: x*y
print(lop(5,2))

#Addition
lop= lambda x,y: x+y
print(lop(3,2))

#Substraction
lop= lambda x,y: x-y
print(lop(3,1))

#Division
lop= lambda x,y: x/y
print(lop(4,3))


x = lambda a: a + 10
print(x(45))

def myfunc(n):
  return lambda a : a * n
mylop = myfunc(5)
print(mylop(10))


str1 = 'arctechnology'
upper = lambda string: string.upper()
print(upper(str1))

str1 = 'arc'
lower = lambda string: string.lower()
print(lower(str1))