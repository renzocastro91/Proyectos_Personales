class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f"${self.amount} - {self.category}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_spending(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

    def get_spending_by_category(self):
        categories = {}
        for expense in self.expenses:
            if expense.category not in categories:
                categories[expense.category] = expense.amount
            else:
                categories[expense.category] += expense.amount
        return categories

    def get_spending_report(self):
        report = ""
        report += "Total Spending:\n"
        report += f"${self.get_total_spending()}\n\n"
        report += "Spending by Category:\n"
        spending_by_category = self.get_spending_by_category()
        for category in spending_by_category:
            report += f"{category}: ${spending_by_category[category]}\n"
        return report


