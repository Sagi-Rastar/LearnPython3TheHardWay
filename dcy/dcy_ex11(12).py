#python中的input
print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#python的input默认被视作字符串类型，执行a+b的时候得到的是两个字符串的连接。
#数据转换的格式{类型()}

#实际上input的提示信息可以直接放在input(这里)
whatif_age = input("plz enter ur age.")
whatif_height = input("plz enter ur height.")
whatif_weight = input("plz enter ur weight.")
print(f"So, you're {whatif_age} old, {whatif_height} tall and {whatif_weight} heavy.^ ^")
#得，人家教程下一篇ex就是这个内容，那我ex12 skip了罢
