from email.utils import encode_rfc2231


print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
#字符串套字符串，用format把snow这个字符串又套进去了
print("And everywhere that Mary went.")
print("." * 10) #uhhhhh分隔符？

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
#一堆字符

#ok
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9+ end10 + end11 + end12)
#没有end = ' '就换行了
#czj在ex1里用的那个是吧（
#目前还没有mistake捏