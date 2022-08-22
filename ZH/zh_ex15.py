from sys import argv

script,filename=argv

txt=open(filename,encoding="utf-8")#打开文件的函数 encoding作用是采用utf8编码 这样就可以读取文件里的中文。

print(f"here is your file {filename}:")
print(txt.read())#.read 告诉python进行文件的阅读。

print("type the filename again:")
file_again=input("> ")

txt_again=open(file_again)

print(txt_again.read())














