import sys
script,input_encoding,error=sys.argv
#encoding参数用来指示编码方式，error参数用来指示发生错误时的处理方法



def main(language_file,encoding,errors):
    line=language_file.readline()
    #if在这起到循环作用（递归于main函数）
    if line:#假如line非空，则进入if
        print_line(line,encoding,errors)
        return main(language_file,encoding,errors)

def print_line(line,encoding,errors):#函数的作用是：将字符串编码为字节，再解码字节。
    next_lang=line.strip()
    #摘自星辉：
    #strip()函数会根据函数体内的字符来扫描字符串从左到右删除前导和尾随的函数体内相应字符得到字符串的相应副本。 
    # 人话：帮你去头去尾，想去啥括号里说 
    raw_bytes=next_lang.encode(encoding,errors=errors)
    #摘自星辉：
    # 从open()里面拿到的是string，所以要encode strings，获得bytes； 

    #读取原始字节 errors=errors 是指输出原始错误信息
    #errors是函数的一个参数，将encode函数中返回的errors赋给errors参数，再输出，即输出原始错误
    cooked_string=raw_bytes.decode(encoding,errors=errors)
    #解码字节
    print(raw_bytes,'<===>',cooked_string)
    #摘自星辉：
    # python在终端里面如果输出的是bytes的话会把bytes写在b' '里面 

languages=open("languages.txt",encoding="utf-8")

main(languages,input_encoding,error)
#摘自星辉：
#   Unicode 统一编码 -> universal encoding 
#   这个编码方案用一个32位的比特（即4个字节）代表一个Unicode字符 | ASCII码表用8位比特（即一个字节）表示一个ASCII字符 
#   然后现在Unicode多于的空间就用来放一些其他（有趣）的东西，比如emoji 
#   因为Unicode实在太浪费了，所以我们一般用8个比特来编码大多数的通用字符； 
#   当我们需要更多的字符时，压缩编码惯例就出来了；//这一段中翻有点绕，看看英文？ 
#   compression encoding convention，压缩编码惯例 
#   需要用到更多空间的时候再用的意思 
#   Unicode Transformation Format 8 Bits > utf-8 
#   在 Python 中，一个字符串就是一个 UTF-8 编码的字符序列，用来显示或者进行文本操作。 
#   DECODE() <> ENCODE() 
#   解码字节 <> 编码字符串

#星辉老师总结的真是太棒辣！