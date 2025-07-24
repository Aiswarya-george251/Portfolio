def add_expense(expense_list, amount, category, date):
    expense = {
        'amount': float(amount),
        'category': category,
        'date': date
    }
    expense_list.append(expense)
    return expense_list

def add_total(expense_list):
    total = 0
    for expense in expense_list:
        total += expense['amount']
    return total

expenses = []

while True:
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    add_expense(expenses, amount, category, date)

    another = input("Do you want to add another expense? (yes/no): ").lower()
    if another != "yes":
        break

print("All Expenses:", expenses)
print("Total Spent:", add_total(expenses))



