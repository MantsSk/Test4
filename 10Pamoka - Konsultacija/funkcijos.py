def basic_calculator(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero!"

    return addition, subtraction, multiplication, division

num1 = float(input("Enter first: "))
num2 = float(input("Enter second: "))

results = basic_calculator(num1,num2)
print(results)


res1 = basic_calculator(5,4)
res2 = basic_calculator(100,60)
res3 = basic_calculator(1000,50)
print(res1)
print(res2)
print(res3)