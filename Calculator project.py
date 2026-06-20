import math


print(f"Henger Calculator")

while True:
    print("Choose a Symbol")
    print("+ is for plus - is for minus * is for time / si for divied by ** is for exponentiation % is for modulus // is for floor division ")
    UserNum =input("Type a Symbol ")

    num1=int(input("Type a number: "))
    num2=int(input("Type your second number: "))


    plus = "+"
    minus = "-"
    time = "*"
    modulus = "%"
    floor_division = "//"
    exponentiation = "**"


    def result():
     if UserNum == "+":
        result = num1 + num2
        return result

    
     if UserNum == "-":
        result = num1 - num2
        return result
    
     if UserNum == "*":
        result = num1 * num2
        return result
    
     if UserNum == "%":
        result = num1 % num2
        return result
    
     if UserNum == "//":
        result = num1 // num2
        return result
    
     if UserNum == "**":
        result = num1 ** num2
        return result

    print(f"The result is: {result()}")





    