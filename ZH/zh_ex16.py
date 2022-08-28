from sys import argv
script,filename =argv


#close - 关闭文件，就像编辑器中的 “文件->另存为”一样。
#read - 读取文件内容。你可以把读取结果赋给一个变量。
#readline - 只读取文本文件的一行内容。
#truncate - 清空文件。清空的时候要当心。
#write('stuff') - 给文件写入一些“东西”。
#seek(0) - 把读/写的位置移到文件最开头。
#cat filename 可以读取文件内容（命令行）s
print(f"we're going to erase {filename}")
print("if you dont want that,hit ctrl-c (^c)")
print("if you do want that,hit return")

input("?")

print("opening the file...")
target=open(filename,'w',encoding="utf-8")#target 就是打开的文件。‘w’代表要对这个文件进行write操作,否则只能打开而不能写入



print("truncating the file.goodbye!")
target.truncate()#进行截断操作。

print("now i am going to ask you for three lines")
#键入新内容
line1=input("line 1:")
line2=input("line 2:")
line3=input("line 3:")

print("i am going to write these to the file")

#写入新内容
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally,we close it")
target.close()#关闭文件







