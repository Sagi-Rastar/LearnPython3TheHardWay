#咋还在printing捏
formatter = """
{}
{}
{}
{}
"""
#留四个坑，用来填
#wowwww，三个双引号真好用捏
print(formatter.format(1, 2, 3, 4))
#填1234
print(formatter.format("one", "two", "three", "four"))
#填1234洋气版
print(formatter.format(True, False, False, True))
#填√xx√
print(formatter.format(formatter, formatter, formatter, formatter))
#每个坑填四个坑
print(formatter.format(
    "uhhhhhhhhhh",
    "actually I don't have anything to say about.",
    "If I have to type sth here...",
    "then, maybe that's it."
))
#填四句话
