'''







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
