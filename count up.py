
number1,number2 = map(int,input("숫자를 입력하세요: ").split())

number2 = number2+1
users = range(number1,number2)

users = list (users)

number2 = number2-1

print(number1,number2)
print (users)