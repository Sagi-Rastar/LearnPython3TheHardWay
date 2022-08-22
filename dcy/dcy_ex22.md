# 总结

## EX1-10 PRINT！
各种print的语法规范 

- 打印内容中如果要在双引号内引用变量的话在前面加一个f
```py
types_of_people = 10
#定义了人的种类数
x = f"There are {types_of_people} types of people."
#将一串描述人的种类数的字符串封装在变量x里
``` 

- 用end = ' '放在printf结尾取消换行
```py
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
```

- 转义字符
```py
#\n	回车符，将光标移到下一行开头。
#\r	回车符，将光标移到本行开头。
#\t	水平制表符，也即Tab键，一般相当于四个空格
#\b	退格（Backspace），将光标位置移到前一列。
#\\	反斜线
#\'	单引号
#\"	双引号
#\	在字符串行尾，即一行未完，转到下一行继续写
```

- format：格式字符串函数，用被应用的字符串中的花括号数量，对应先后顺序往里面填
```py
joke_evaluation = "Isn't that joke so funny?! {}"
#字符串变量，注意双引号前没有加f
print(joke_evaluation.format(hilarious)) 
```
```py
#没有引用变量的.format
print("Its fleece was white as {}.".format('snow'))
#字符串套字符串，用format把snow这个字符串又套进去了
```

- 三个引号可以瞎写
```py
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 line if we want, or 5, or 6.
wowwwwwww
really?
exactly
""")
``` 

## EX11-17 INPUT！
获得用户input的方法，与操作外部文件
- script内input
    - input(内放字符串，用于提示)
    ```py
    whatif_age = input("plz enter ur age.")
    whatif_height = input("plz enter ur height.")
    whatif_weight = input("plz enter ur weight.")
    ```
- script外input
    - 命令行输入时，跟在python 后面的叫做argv，并需要在script内开头解包
    ```py
    scr, first, second, third = argv

    print("The script is called:", scr)
    print("Your first variable is :", first)
    print("Your second variable is:", second)
    print("Your second variable is:", third)
    ```
    
    - 初识调用外部文件，文件对象相当于DVD，先要open()才能read()最后记得close()
    ```py
    txt = open(filename)
    #open()
    #"打开"（存放）某一文件，并且将内容存储在{txt}这个文件对象中

    print(f"# Here's your file {filename}:")
    print("---")
    print(txt.read())
    ```
    
    - 读写外部文件，常用调用外部文件函数：
    ```py
    #filename_test:dcy_ex16_test.txt
    #open - “存放”文件，w模式也就是write
    #close - 关闭文件，就像编辑器中的 “文件->另存为”一样。
    #read - 读取文件内容。你可以把读取结果赋给一个变量。
    #readline - 只读取文本文件的一行内容。
    #truncate - 清空文件。清空的时候要当心。
    #write('stuff') - 给文件写入一些“东西”。
    #seek(0) - 把读/写的位置移到文件最开头。
    #exists() - 检测文件是否存在，返回布尔值。
    ```

## EX18-21 FUNCTION!
函数声明写法，及调用方法
- 定义函数的方法
```py
# this one is like your scripts with argv
# 另详见czj的ex18文件
def print_two(*args): # 一个*跟变量表示一个元组
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
```

- 函数形参赋值方法
```py
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
```

- 函数与操作外部文件
```py
貌似没啥讲的（
```