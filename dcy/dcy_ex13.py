#filename: dcy_ex13.py
from sys import argv
#read the WYSS(?) section for how to run this
scr, first, second, third = argv

print("The script is called:", scr)
print("Your first variable is :", first)
print("Your second variable is:", second)
print("Your second variable is:", third)

#这次的脚本不能直接从VScode里面编译，因为他要在一开始的命令行里面就给另外后面三个参数
#因此记得在终端里面直接输入|python urname_ex13.py {变量1} {变量2} {变量3}|
#这次属于另外一种input方法
#英文：parameters，unpacking，variables
#中文：参数，解包，变量
#
#名词解释：
#arg -> arguments：命令行参数 
#argv -> arguments variable：参数 变量
#features -> modules：功能，模块，库；就是第2行那的导入，类似于c
#
#在终端内输入的|python {your_filename} {变量1} {变量2} {变量3}|
#这里的{your_filename}就是arg，后面的{变量123}就是所谓的v，两者合起来就是argv
#所以这段程序里的第三行就是python的解包过程，写在最上面，将argv的值用前4个名字解包
#
#Q&A：
#Q：arg一定要用script这个名字解包吗？
#A：显然不是，我用scr一样可以，只是一个解包名字
#
#tips：
#终端里面用|cd {文件所在路径}|进入文件所在路径
#现在你的终端就相当于进了这个文件夹了
#然后再输入22行的内容