types_of_people=10
x=f"there are {types_of_people} types of people"#给x赋了一个字符串

binary="binary"
do_not="don't"
y=f"those who know {binary} and those who {do_not}"#给y赋了一个字符串

print(x)
print(y)

print(f"i said:{x}")
print(f"i also said:'{y}'")


hilarious=False
joke_evaluation="isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))
#.format()会把括号中的内容填入字符串的花括号中，作为f字符串的替代方法。
w="this is the left side of "
e="a string with a right side."

print(w+e)#合并字符串 太简单了8！吊打c