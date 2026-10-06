# Expense Tracker - Installment 3
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

item2 = input ("Second Expense? ")
amount2 = float (input ("Amount? "))
subtotal = subtotal + amount2

tax_percent = int (input("Tax Rate (%)? "))
budget = float (input("Budget? "))
average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print ("-" * 40)
print ("SUMMARY")
print ("\t-", item1, ":" , "\t$", amount1)
print ("\t-", item2, ":" , "\t$", amount2)
print ("Subtotal:\t\t$", subtotal)
print ("Average:\t\t$", average)
print ("Tax:\t\t\t$", tax)
print ("Total:\t\t\t$", total)
print ("Over the Budget?\t", over_budget)
print ("Left in budget:\t\t$", left)
print ("-" * 40)
print ("Made by: Tanya Anrachel M. Labanes | Installment 3")
