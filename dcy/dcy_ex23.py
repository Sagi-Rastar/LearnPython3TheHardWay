#filename:dcy_ex23.py
import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
        # main函数调用自己，形成loop，结束循环的条件是if line，最后遇到空的字符串的时候就会停止loop


def print_line(line, encoding, errors):
    next_lang = line.strip()
    # strip()函数会根据函数体内的字符来扫描字符串从左到右删除前导和尾随的函数体内相应字符得到字符串的相应副本。
    # 人话：帮你去头去尾，想去啥括号里说
    # strip > v.除去，撕掉
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # 从open()里面拿到的是string，所以要encode strings，获得bytes；
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # 为了打印出来bytes和strings对照，所以对raw_bytes逆向展示为cooked_strings,raw是bytes，所以要decode
    print(raw_bytes, "<===>", cooked_string)
    # python在终端里面如果输出的是bytes的话会把bytes写在b' '里面


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)
# 这作者从01讲编码还是讲的不错的
#   Unicode 统一编码 -> universal encoding
#       这个编码方案用一个32位的比特（即4个字节）代表一个Unicode字符 | ASCII码表用8位比特（即一个字节）表示一个ASCII字符
#       然后现在Unicode多于的空间就用来放一些其他（有趣）的东西，比如emoji
#   编码惯例？
#       因为Unicode实在太浪费了，所以我们一般用8个比特来编码大多数的通用字符；
#       当我们需要更多的字符时，压缩编码惯例就出来了；//这一段中翻有点绕，看看英文？
#       compression encoding convention，压缩编码惯例
#       需要用到更多空间的时候再用的意思
#       Unicode Transformation Format 8 Bits > utf-8
#       在 Python 中，一个字符串就是一个 UTF-8 编码的字符序列，用来显示或者进行文本操作。
#       DECODE() <> ENCODE()
#       解码字节 <> 编码字符串