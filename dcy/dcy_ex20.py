#filename:dcy_ex20.py
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
# 读取文件|？为啥不用open了

def rewind(f):
    f.seek(0)
# 将文件指针放到开头，seek()的作用是将文件的读取指针放到括号里的第几个字节处

def print_a_line(line_count, f):
    print(line_count, f.readline(),end = " ")
# readline()的作用：打印第{line_count}行的文字
# readline执行一遍之后会将指针，停在\n后面，并且打印\n以前该行的字符串。（注意，\n也保留在里面）

current_file = open(input_file)
# 哦我傻了，上面是函数定义，这里才开始open

print("First let's print the whole  file:\n")

print_all(current_file)

print("Now, let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)















