#Generates a brand name from a list of questions inputted by the user.

print("Hi there! Welcome to the Brand Name Generator. Kindly follow all the prompts to get your cool Band name.")
user_city = input("Enter the name of city you grew up in:\n")
user_pet = input("Enter your pet name:\n")
brand_name = user_city + " " + user_pet
print("Well, " + brand_name + " could be a good brand name.")




#Bill Splitter with Tip Calculator

print("Welcome to the tip calculator")
bill = float(input("What is the total bill? "))
percent = float(input("What percentage would you like to split with? 10, 12, or 15? "))
people = int(input("How many people will split the bill? "))
split_bill = (bill/people) + ((bill/people) * (percent/100))
split_bill_round = "{:.2f}".format(split_bill, 2)
#this line fixes the formatting error of Python when it doesn't include double decimal points for zeroes. The .format(split_bill) can also be used since 2decimal point has been indicated with the :.2f.
message = f"Each person should pay: {split_bill_round}"
print(message)
