number = int(input("set a number: "))

reverseNumber = 0

while (number > 0):
    digit = number % 10
    print(digit)
    reverseNumber = reverseNumber * 10 + digit
    print(reverseNumber)
    number = number // 10
    print(number)

print("Numero invertido igual a %d" %(reverseNumber))
