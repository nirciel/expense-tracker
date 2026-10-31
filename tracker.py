# Expense Tracker - Installment 5
# Author: Tanya Anrachel M. Labanes
# Description: This program allows users to track their expenses and income.

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tTrack your expenses and income with ease.")
print("=" * 40)

name = input("What is your name? ")
tax_percent = float(input("Tax Rate %? "))
budget = float(input("Your Budget? "))

subtotal = 0
count = 0

print("Welcome, ", name, "!")
print("\nMAIN MENU")
print(" [1] Add an Expense")
print(" [2] View all Expenses (coming soon)")
print(" [3] Show total spent")
print(" [4] Exit")

choice = ""

while choice != "4":
    

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal = subtotal + amount
        count = count + 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        gtotal = subtotal + tax
        over_budget = gtotal > budget
        left = budget - gtotal

        print("Expense Count:\t" + str(count))
        print("Subtotal:\t$", subtotal)
        print("Tax (" + str(tax_percent) + "%):\t$", tax)
        print("Grand Total:\t$", gtotal)

        if over_budget:
            print("Over budget by: $", left * -1, "!")
        elif gtotal > budget * 0.9:
            print("Careful: only   $", left, "left.")
        else:
            print("Within budget.   $", left,"left.")

    elif choice == "4":
        print("Goodbye, " + name + "!")
        print("-" * 40)
        print("Made by: Tanya Anrachel M. Labanes | Installment 5")
        print ("=" * 40)

    else:
        print("  Please choose 1, 2, 3 or 4.")

