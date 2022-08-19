#filename:dcy_ex16.py
#filename_test:dcy_ex16_test.txt
#close - 关闭文件，就像编辑器中的 “文件->另存为”一样。
#read - 读取文件内容。你可以把读取结果赋给一个变量。
#readline - 只读取文本文件的一行内容。
#truncate - 清空文件。清空的时候要当心。
#write('stuff') - 给文件写入一些“东西”。
#seek(0) - 把读/写的位置移到文件最开头。
#
#wow,我们要做编辑器了捏

from sys import argv

scrpt, filename = argv

print(f"We're going to erase {filename}.")
print("If u don't want that, hit CTRL-C (^C).")
print("If u do want that, hit RETURN.")

input("? ")

print("Opening the file...")
target = open(filename, 'w')
#open(file, mode = '{mode,default:r}')

print("Truncating the file. Goodbye!")
target.truncate()
#Q：如果没有清空呢
#A：write模式会从头开始编辑，原有内容会被删除。

print("Now I'm going to ask u for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")


print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# 这样写入，太勾八了

print("And finally, we close it.")
target.close()
