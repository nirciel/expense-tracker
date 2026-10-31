# Expense Tracker - Installment 4
# Author: Tanya Anrachel M. Labanes
# Description: This program is called an "Expense Tracker" which allows the users to track their expenses and income. 

print ("=" * 40)
print ("\t\tEXPENSE TRACKER")
print ("\tTrack your expenses and income with ease.")
print ("=" * 40)
print ("MAIN MENU")
print (" [1] Add an Expense\t\t(coming soon)")
print (" [2] View all Expenses\t\t(coming soon)")
print (" [3] Show total spent\t\t(coming soon)")
print (" [4] Exit\t\t\t(coming soon)\n")


name = input("What is your name? ")
print ("Welcome, ",name , "! Let's log two expenses.\n")
subtotal = 0

item1 = input ("First Expense? ")
amount1 = float (input ("Amount? "))
subtotal = subtotal + amount1

if amount1 < 50:
    print ("  Small expense.")
elif amount1 >= 50 and amount1 <= 100:
    print ("  Moderate expense.")
elif amount1 > 100 and amount1 <= 200:
    print ("  Big expense.")
else:
    print ("  Huge expense - are your sure?")


item2 = input ("Second Expense? ")
amount2 = float (input ("Amount? "))
subtotal = subtotal + amount2

if amount2 < 50:
    print ("  Small expense.")
elif amount2 >= 50 and amount2 <= 100:
    print ("  Moderate expense.")
elif amount2 > 100 and amount2 <= 200:
    print ("  Big expense.")
else:
    print ("  Huge expense - are your sure?")

if amount1 >= 100 and amount2 >= 100:
    print ("  Two big expenses in a row - slow down!")

tax_percent = float (input("Tax Rate %? "))
budget = float (input("Your Budget? "))
average = subtotal / 2
tax = subtotal * (tax_percent / 100)
gtotal = subtotal + tax
over_budget = gtotal > budget
left = budget - gtotal

print ("-" * 40)
print ("SUMMARY")
print ("\t-", item1, ":" , "\t$", amount1)
print ("\t-", item2, ":" , "\t$", amount2)
print ("Subtotal:\t\t$", subtotal)
print ("Average:\t\t$", average)
print("Tax (" + str(tax_percent) + "%):\t\t$" + str(tax))
print ("Grand Total:\t\t$", gtotal)

if over_budget:
    print("Over budget by: $" + str(left * -1) + "!")
elif gtotal > budget * 0.9:
    print("Careful: only $" + str(left) + " left.")
else:
    print("Within budget. $" + str(left) + " left.")

print ("-" * 40)
print ("Made by: Tanya Anrachel M. Labanes | Installment 4")
