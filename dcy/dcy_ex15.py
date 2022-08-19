#filename:dcy_ex15.py
#filename_sample:dcy_ex15_sample.txt
#调用外部文件
from sys import argv

script, filename = argv

txt = open(filename)
#open()
#"打开"（存放）某一文件，并且将内容存储在{txt}这个文件对象中

print(f"# Here's your file {filename}:")
print("---")
print(txt.read())
#{变量}.read
#替换变量为文件内容
print("---")

print("# Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print("---")
print(txt_again.read())
print("---")

txt.close()
txt_again.close()