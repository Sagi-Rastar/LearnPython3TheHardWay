#filename:dcy_ex33
#while-loop
# while 后面跟着的是布尔表达式
from cgi import test


 
# 一个列表   还记得吗，用中括号表示列表。

def print_loop_i(a):
    i = 0 
    # 一个变量
    numbers = []
    while i < a:
        # python里面的i初始化要在前面做。
        print("-" * 10)
        print("Numbers now: ", numbers)
        print(f"Now I gonna add {i} .")
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print(f"Next i is {i}.")

print("The numbers: ")
numbers = []

for num in numbers: # num是形参，把numbers这个列表里的所有东西打印出来。
    print(num)

print_loop_i(9)

# 如果后面的列表是二维数组会怎么样？
test = [[1, 2, 3],[4, 5, 6]]
for te in test:
    print(te)
# output:
# [1, 2, 3]
# [4, 5, 6]