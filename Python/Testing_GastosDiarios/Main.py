from ClasesGastosDIarios import *

#El programa permitirá al usuario ingresar sus gastos y categorizarlos en 
# diferentes tipos de gastos, como alimentación, transporte, entretenimiento, 
# etc. Luego, el programa mostrará un resumen de los gastos del usuario y los 
# ordenará por categoría.
# Testing
tracker = ExpenseTracker()

expense1 = Expense(15.50, "Food")
expense2 = Expense(20.00, "Transportation")
expense3 = Expense(12.75, "Entertainment")

tracker.add_expense(expense1)
tracker.add_expense(expense2)
tracker.add_expense(expense3)

print(tracker.get_spending_report())
