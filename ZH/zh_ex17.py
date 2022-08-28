from sys import argv
from os.path import exists

script,from_file,to_file=argv
#复制文件内容
print(f"copying from {from_file} to {to_file}")

in_file=open(from_file,encoding="utf-8");indata=in_file.read()#获得in_file的内容
#由此可见“；”在python中也可以起到分隔语句的作用。

print(f"the input file is {len(indata)} bytes long")#len()可以测文件占用字节长度
print(f"dose the output file exist?{exists(to_file)}")#验证文件是否被创建成功 返回true 或 false
print("ready,hit return to continue,ctrl-c to abort")
input()

out_file=open(to_file,"w")
out_file.write(indata)#写入in_file的内容

print("alright,all done.")

out_file.close()
in_file.close()