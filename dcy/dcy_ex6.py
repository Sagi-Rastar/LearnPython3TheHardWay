from tkinter import W


types_of_people = 10
#定义了人的种类数
x = f"There are {types_of_people} types of people."
#将一串描述人的种类数的字符串封装在变量x里

binary = "binary"
#定义一个字符串变量
do_not = "don't"
#同上
y = f"Those who know {binary} and those who {do_not}."
#一串引用了两次字符串变量的字符串，并且封装在y里//第一，第二处

print(x)
print(y)
#输出

print(f"I said: {x}")
print(f"I also said: '{y}'")
#阿巴阿巴，继续输出，这里注意x和y是变量，需要写花括号//第三，第四处
#……应该就四处吧，下面那个hil的变量应该是布尔数

hilarious = False
#变量“好笑程度” no，不好笑
joke_evaluation = "Isn't that josk so funny?! {}"
#字符串变量，注意双引号前没有加f
print(joke_evaluation.format(hilarious))
#草，梦回面向对象，format()函数的作用？转换类型？
#format：格式字符串函数，用被应用的字符串中的花括号数量，对应先后顺序往里面填

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
print(w,e)
#加号的区别
