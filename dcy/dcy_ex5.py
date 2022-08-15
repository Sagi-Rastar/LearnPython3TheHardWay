my_name = 'dcy'
my_age = 19 # 20 this year
my_height = 175 # meter
my_weight = 75 # kilo, maybe()
my_eyes = 'Brown'
my_teeth = 'White' # for sure
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} meters tall.")
print(f"He's{my_weight} kilos heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.") # yeeeee

#this line is tricky, try to get it sxactly right
total = round(my_age + my_height + my_weight,2)
#嘻嘻摸鱼就不写转换了！
#round(x,y) | x = 被舍入数 ， y = 保留位数
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
#捏妈我还以为等号前后有空格是python严格缩进限制的
#test