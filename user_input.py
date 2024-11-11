
def mathOperators(a, b, c):
    addition = "+"
    subtraction = '-'
    multiplication = '*'
    divition = '/'
    
    if c == addition:
        answer = a + b
        return answer
    elif c == subtraction:
        answer = a - b
        return answer
    elif c == multiplication:
        answer = a * b
        return answer
    elif c == divition:
        answer = a / b
        return answer
    else:
        return "You have entered an invalid sign"
        
input1 = int(input("enter first number: "))
input2 = int(input("enter second number: "))
operator = input("enter a '+' or '-', or '*', '/' sign: ")

result = mathOperators(input1, input2, operator)
print(result)
            