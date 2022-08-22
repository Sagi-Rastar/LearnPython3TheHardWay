#Wow, function!
#filename:dcy_ex18.py

# this one is like your scripts with argv
def print_two(*args): # 一个*跟变量表示一个元组
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually ponitless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Hey!", "you!")
print_two_again("Yeah!", "That's it!")
print_one("ONLY U!")
print_none()

#python里面的定义函数用def啊草
#python严格缩进的特性有所耳闻，结束函数居然也是另起一行不缩进（
#↑个屁
#作者是怎么解释*的
#*args 中的 * 是什么作用？
#这是告诉 Python 取所有的参数给函数，然后把它们放在 args 里放成一列。
#实际上是元组