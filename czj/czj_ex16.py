from sys import argv

script,filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that,hit CTRL-C(^C).")
print("If you want that,hit RETURN.")

input("?")

#打开文件
print("Opening the file...")
target = open(filename,'w')

#清空文件
print("Truncating the file.Goobye!")
target.truncate()

print("Now I'm going to ask you for three line.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file.")

#写入
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally,we close it.")
target.close()