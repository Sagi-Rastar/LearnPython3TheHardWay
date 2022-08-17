from re import T


formatter="""
{}
{}
{}
{}
"""#三个双引号可以输入跨行格式的字符串，输出时也会保留这种格式
#formatter相当于挖了四个空 让format函数填进去

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))#递归输出“{}”4*4=16个
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"

))

lines=(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)

print(repr(lines))#repr函数输出原始字符串内容
print(formatter.format(*lines))#指针？
print(lines)#输出内容与repr相同
