#仍然是类似于c里面的通用规则：转义字符
from imghdr import what
from turtle import back


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

what_if = '''
what_if?
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(what_if)
