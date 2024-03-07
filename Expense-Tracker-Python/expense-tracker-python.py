class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.categories = {}

    def add_expense(self, date, amount, category):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append((date, amount))

    def add_expense_category(self, category):
        if category not in self.categories:
            self.categories[category] = 0

    def view_expenses(self):
        for category, items in self.expenses.items():
            total_amount = sum(amount for _, amount in items)
            print(f"{category}: ${total_amount}")

    def view_expense_categories(self):
        print("Categories:")
        for category in self.expenses.keys():
            print(category)

# basic usage
tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Add Expense Category")
    print("3. View Expenses")
    print("4. View Expenses Categories")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter Expense date (YYYY-MM-DD): ")
        amount = float(input("Enter Expense amount: $"))
        category = input("Enter Expense category: ")
        tracker.add_expense(date, amount, category)
    elif choice == "2":
        category = input("Enter Expense category: ")
        tracker.add_expense_category(category)
    elif choice == "3":
        tracker.view_expenses()
    elif choice == "4":
        tracker.view_expense_categories()
    elif choice == "5":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
