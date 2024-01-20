#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = 150.00
bill_split = bill/5
split_with_tip = bill_split * 1.12
print(format(split_with_tip, ".2f"))

print("Welcome to the tip calculator.")
total = input("What was the total bill?\n$")
tip = input("What percentage tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")
total_with_tip = float(total) + ((int(tip) * .01) * float(total))
split = float(total_with_tip) / int(people)
print(f"Each person should pay: ${format(split, ".2f")}")