def sum(a,b,*c):
    print(c)
    print(type(c))
    sum = a+b
    for i in c:
       sum = sum + i
    return sum
print(sum(24,25,68,7896,25,1,23))

# with keywords we pass ** in arguments
def sum(**args):
    # print(type(args))
    sum=0
    # print(args)
    for i,j in args.items():
        print(i,j)
        sum+=j
    return sum
print(sum(num3=36,num4=-50,num6=199,num2=25,num8=122))

# scope
num1=25
def trail():
    b=50
    global num1
    num1=50
    print(num1)
    print(b)
trail()
print(num1)

# recursion:function calling itself

def fact(n):
#    print(n)
   if n==1:
       return 1
   temp=fact(n-1)
   print(temp)
   return n*temp 
res=fact(5)
print(res)

# decorators
def function_decorator(func):
    def wrapper():
        print("please check your a4 sheets")
        func()
        print("Thank U!")
    return wrapper
@function_decorator
def printer():
    print("printing.......")
printer()

