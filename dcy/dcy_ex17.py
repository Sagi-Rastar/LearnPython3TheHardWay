#filename:dcy_ex17.py
#filename_test:dcy_ex17_test.txt
#filename_test_new:dcy_ex17_test_new.txt


from genericpath import exists

from sys import argv

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file) ; indata = in_file.read()
#HA! ONE LINE!

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

#terminal:
#echo |echo "双引号内填写入的内容" > {文件}|写入，为啥非得用打印这个术语（
#cat 显示文件内的内容。
#Q&A:
#Q：close()的作用？
#A：close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。
#人话A：这个文件一直都会被占用，不能再被操作
#Q：有无好哥哥讲一下句柄是啥玩意，查百度查了半天看不懂a，是类似于地址吗