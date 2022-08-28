
#相当于先定义子函数，再在主函数中顺序执行。

#定义：
    #*args 是指针 def是definition的缩写 即用于定义的函数。
    #定义了一个函数print_two *args是函数的参数（指针型）也可以直接定义多个变量
    #这个函数的作用是：打印args里的两个变量的内容到一个字符串中。
def print_two(*args):#冒号下的内容必须按一次tab对齐，否则出错
    arg1,arg2=args
    print(f"arg1:{arg1},arg2:{arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():
    print("i got nothin'")


#执行：
print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first")
print_none()















