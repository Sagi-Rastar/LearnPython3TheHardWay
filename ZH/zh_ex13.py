import antigravity
from sys import argv
#一种神秘的初始化语句 总之写上后可以调用argv这个含有四个参数的变量。

#名词解释：
#arg -> arguments：命令行参数 
#argv -> arguments variable：参数 变量
#这里的{your_filename}就是arg，后面的{变量123}就是所谓的v
#                                   -------by sagi—rastar
#即从命令行里读取(解包)参数的变量

script,first,second,third = argv
print("the script is called:",script)#script 就是文件名 不是一个可用参数
#记住与c不同 逗号是分割两个不同打印语句的
print("your first variable is:",first)
print("your second variable is:",second)
print("your third variable is:",third)

#多于或少于三个值都会报错，必须定义四个参数 否则也报错








