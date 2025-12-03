'''
string subscripting=> print("Hello"[0])
primitive data types=>sting, integers, float(decimal), boolean(true. false)
type function=> print(type("Hello"))
type conversion/casting=> print(int("123")+ int("456"))
mathematical operation=> +, -, *, /, //( single slash for floating o/p and // for int o/p, It 
does not round off the no but remove the digits after decimal point). **(exponential/power)
priority sequence PEMDAS=> (),**,*,/,+,-
rounding function=> 
bmi = 78/ 1.43 ** 2
print(round(bmi,2))
assignment operator=> +=. -=, *=, /=
f-strings=> to insert a variable or an expression into a string.

score =0
height = 1.8
is-winning = True
print(f"Your score is = {score}, your height is {height}. Your are winning is {is_winning}")


coding exercise 4=> BMI Calculator
height = 1.65 
weight = 84
bmi = 84 / ( 1.65 ** 2 )

'''

print("Click Run to run the final project you will build")
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12, or 15?"))
no_of_people = int(input("How many people to split the bill?"))
each_person = (total_bill * (tip/100) + total_bill) / no_of_people
#each_person = (total_bill * (1 + tip / 100)) / no_of_people
each_person = round(each_person, 2)
print(f"Each person should pay: ${each_person}")
