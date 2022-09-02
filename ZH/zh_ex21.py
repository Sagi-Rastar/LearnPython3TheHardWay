def add(a,b):
    print(f"adding {a}+{b}")
    return a+b

def subtract(a,b):
    print(f"subtracting {a}-{b}")
    return a-b


def multiply(a,b):
    print(f"multiplying {a}*{b}")
    return a*b

def divide(a,b):
    print(f"dividing {a}/{b}")
    return a/b
#return 与c无异 不用括号。
print("lets do some math with just functions!")

age=add(30,5)#35
height=subtract(78,4)#74
weight=multiply(90,2)#180
iq=divide(100,2)#50

print(f"age:{age},height:{height},weight:{weight},iq:{iq}")

what=add(age,subtract(height,multiply(weight,divide(iq,2))))#35+（74-（180*（50/2）））=

print(what)







