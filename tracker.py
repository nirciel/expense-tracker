# Expense Tracker - Installment 2
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
item1 = input ("First Expense? ")
amount1 = float (input ("Amount? "))
item2 = input ("Second Expense? ")
amount2 = float (input ("Amount? "))
total = amount1 + amount2
average = total / 2
print ("-" * 40)
print ("SUMMARY")
print ("\t-", item1, ":" , "\t$", amount1)
print ("\t-", item2, ":" , "\t$", amount2)
print ("Total Spent:\t\t$", total)
print ("Average:\t\t$", average)
print ("-" * 40)
print ("Made by: Tanya Anrachel M. Labanes | Installment 2")
