#filename:dcy_ex32.py
#循环&列表
#hairs = ['brown', 'blond', 'red']
#eyes = ['brown', 'blue', 'green'] weights = [1, 2, 3, 4]
#
#for-loop
from __future__ import print_function


the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixes lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can  also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
# append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Elements was: {i}")

#for循环就是将变量依次取序列里面的值，
#每取一次后面的值就执行一次下面的代码块，
#直到所有的值取完。

#跟c的区别是没有第二个分号判断条件，如果要判断得要自己写。