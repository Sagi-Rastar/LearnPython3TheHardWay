#设计函数参数时，如果使用两个**符号后跟字母，表示这个参数是一个列表
def print_two(**args):
    tmp = args
    print(tmp)

#我们在设计函数参数的时候，如果使用一个*符号后跟字母，表示这是一个元组
def print_w(x,y,*args,):
    tmp = args
    print(tmp)
    print(tmp[0])
    print(x)
    print(y)


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

a = "Zed";b = "Shaw";c = "flow"
ar = (a,b,c)
br = (a,c,b)
cr = (b,c,a)

print_two(a = 1,b = 2,c = 3)
print_w(a,b,c)
print_w(ar,br,cr,ar)

print_two_again(a,b)
print_one(a)
print_none()