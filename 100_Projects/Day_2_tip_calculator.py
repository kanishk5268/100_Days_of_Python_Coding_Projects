print("Welcome to the tip calculator \n")
total_bill = float(input("What was the total bill? \n"))
percent_tip = float(
  input("What percentage tip would you like to give? 10, 12, or 15? \n"))

no_of_people = int(input("How many people to split the bill? \n"))

each_split = round(
  ((total_bill) + ((percent_tip / 100) * total_bill)) / no_of_people, 2)

print(each_split)
