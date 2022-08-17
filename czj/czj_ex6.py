#定义一个看起来像二进制数的整数
types_of_people = 10
x = f"There are {types_of_people} types of people."
#定义一些很奇怪的字符串
binary = "binary"
do_not = "don't"
#这里两处字符串套字符串
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
#这算一处
print(f"I said: {x}")
#这算一处
print(f"I also said: '{y}'")

hilarious = False
flows = True

joke_evaluation = "Isn't that joke so funny?! {}{}{}"
#有format{}会被特殊处理，能填东西
print(joke_evaluation.format(hilarious,' ',flows))
print(joke_evaluation)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)