#引入了输入函数
#python的input默认被视作字符串类型，执行a+b的时候得到的是两个字符串的连接。
print("how old are you?",end='')
age=int(input())#int() 限制了输入内容必须是整数 而不是把数字转换成整数
print("how tall are you?",end='')
height=input()
print("how much do you weigh?",end='')
weight=input()

print(f"so you are {age} old,{height} tall and {weight} heavy")










