from sys import argv
#读取文件名
script,filename = argv
#打开文件
txt = open(filename)
#输出莫名其妙的东西
print(f"Here's your file {filename}:")
#输出文件内容
print(txt.read())
#再次输入文件名
print("Type the filename again:")
#输入引导
file_again = input(">")
#打开文件
txt_again = open(file_again)
#输出文件内容
print(txt_again.read())
txt.close()
txt_again.close()
