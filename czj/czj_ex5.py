my_name = 'Flows'
my_age = 19 # not a lie
my_height_m = 172 # m
my_weight_kg = 52 # kg
#1 英尺=0.3048 米
my_height_inches = round(my_height_m * 0.3048,2)
#1 磅=0.45359237 千克(kg)
my_weight_pounds =  round(my_weight_kg * 0.45359237,2)
my_eyes = 'Black'
my_teeth = 'White' #md前几天去看牙蛀了好几颗，还有两颗要做根管根管，还tm不给报销，我真是
my_hair = 'Black'
print(f"Let's talk about {my_name}.")
print(f"He's {my_height_inches} inches tall.")
print(f"He's {my_weight_pounds} pounds heavy.")
print("It can also say,")
print(f"He's {my_height_m} m tall.")
print(f"He's {my_weight_kg} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = round(my_age + my_height_inches + my_weight_pounds,2)
print(f"If I add {my_age}, {my_height_inches}, and {my_weight_pounds} I get {total}.")