#车的数量
cars = 100
#每辆车的容量
space_in_a_car = 4
#司机人数
drivers = 30
#乘客数
passengers = 90
#开不了的车的数量，因为一个司机只能开一辆车
cars_not_driven = cars - drivers
#开的车的数量，即司机数
cars_driven = drivers
#总容量
carpool_capacity = cars_driven * space_in_a_car
#平均每辆车坐多少人
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")

#1.soace_in_car 会变成整型，carpool_capacity也会变成整型
x = 1
y = 1
z = x + y
print("1 + 1 = ",z)