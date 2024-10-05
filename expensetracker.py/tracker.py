import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file)

    def add_expense(self, amount, category, description):
        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        for idx, expense in enumerate(self.expenses, start=1):
            print(f"{idx}. {expense['description']}: ${expense['amount']} in category '{expense['category']}'")

    def summarize_expenses(self):
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

        print("Expense Summary by Category:")
        for category, total in summary.items():
            print(f"{category}: ${total}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Expenses: ${total}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses by Category")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.summarize_expenses()
        elif choice == '4':
            tracker.total_expenses()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
