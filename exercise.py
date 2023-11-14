num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
sum = num1 + num2
substraction = num1 - num2
multiplication = num1 * num2
division = num1 // num2
div = num1 / num2
power = num1 ** num2
modulus = num1 % num2

# inputing number using input() method

print(' sum of two numbers is :',sum)
print('substraction of two numbers is :',substraction)
print('multiplication of two numbers is :',multiplication)
print('division of two numbers is :',division)
print('division of two numbers is :',div)
print('division of two numbers is :',num1,'and', num2,'equal',division)
print('power of two numbers is :',power)
print(' modulus of two numbers is :',modulus)

# input the name and then create a list of those inputed name and sort them according to alphabetical order


createList = []

length  = 4
for i in range(length):
    name = input("Enter the names:").capitalize()
    # capitizeName = name.capitalize()
    createList.append(name)

sortedList = sorted(createList)
print(sortedList)
