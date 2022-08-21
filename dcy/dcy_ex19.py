#filename:dcy_ex19.py

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"NOW! You have {cheese_count} cheeses!")
    print(f"NOW! You have {boxes_of_crackers} boxes of crackers!")
    print("COOOOOOL!! Man that's enough for a party!")
    print("Get a blanket.\n")

def howmuch_cc_now():
    print(f"Now u have {a} cheese, {b} crackers.")
# uh 有个问题啊，python里面的形参没有定义数据类型啊，默认是啥，字符串还是自动的啊
# 而且啊，python函数甚至不用自己定义返回值类型的么

print("We can just give the funtion numbers directly:")
cheese_and_crackers(20, 30)
# 第一种赋值方法；直接给实参的位置赋值

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# 第二种赋值方法；给实参起名字，然后单独赋值

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# 第三种赋值方法：实参内支持数学运算

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# 第四种赋值方法；实参内的数学运算支持用变量
# yummy!

a = input("how much cheese do u want?")
b = input("how much crackers do u want?")
howmuch_cc_now(howmuch_cc_now())
