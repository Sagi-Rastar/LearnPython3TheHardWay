from sys import argv
script,input_file=argv

def print_all(f):#读取并打印f里所有内容
    print(f.read())
#使用后文件读取指针在文件末尾
def rewind(f):#重置文件读取指针，使得可以再一次从头读取
    f.seek(0) #seek()的作用是将文件的读取指针放到括号里的第几个字节处 

def print_a_line(line_count,f):#逐行读取并且打印f的内容
    print(line_count,f.readline())#line_count计数了当前的行数
# readline()的作用：打印第{line_count}行的文字 
# readline执行一遍之后会将指针，停在\n后面，并且打印\n以前该行的字符串。（注意，\n也保留在里面） 

current_file=open(input_file)

print("first lets print the whole file:\n")

print_all(current_file)
print("now lets rewind,kind of like a tape")

rewind(current_file)
print("lets print three lines:")

current_line=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)

