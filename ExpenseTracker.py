import os
width = os.get_terminal_size().columns

class Expense:
    def __init__(self,amount,category,description,date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
    def __str__(self):
        return f"amount: ${self.amount} | category: {self.category} | description: {self.description} | date: {self.date}\n"
 
# ex = Expense(200,'Food','Takes dinner in a restaurent.','12-09-56')
# print(ex)

class Category:
    def __init__(self,name,budget=None):
        self.name = name
        self.budget = budget
        self.total_spent = 0
    def checkBudget(self, amount):
        if self.budget and (self.total_spent + amount) > self.budget:
            print(f"Warning: Spending exceeds the budget for {self.name}!\n")
        self.total_spent += amount

# ca = Category("Food",100)
# ca.checkBudget(50)
# ca.checkBudget(40)
# ca.checkBudget(20)

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = {}
    def addCategory(self,name,budget = None):
        self.categories[name] = Category(name, budget)
    def addExpense(self, amount, category, description, date):
        # Adds a new expense to the tracker.
        if category not in self.categories:
            print("Category not found!")
            return
        expense = Expense(amount,category,description,date)
        self.categories[category].checkBudget(amount)
        self.expenses.append(expense)

    def viewExpenses(self):
        print("'Expense lists'".center(width))
        # Displays all recorded expenses.
        for expenses in self.expenses:
            print(expenses)
    def getTotalExpenses(self):
        # Returns the total amount spent across all categories.
        total_expense = 0
        for expense in self.expenses:
            total_expense += expense.amount
        print(f"The total Expenses across all categories are : ${total_expense}\n")
    def generateReport(self):
        # Generates a report by category.
        print("\t---'Report Card'----")
        print("Category\tBudget\tTotal_Expenses")
        print("--------\t-------\t--------------")
        for name,obj in self.categories.items():
            print(f"{name}\t\t${obj.budget}\t${obj.total_spent}\n")


#creating object
myTracker = ExpenseTracker()

#adding categories
myTracker.addCategory("Food",5000)
myTracker.addCategory("Travel",3000)
myTracker.addCategory("Clothes",4000)

#adding expenses
myTracker.addExpense(100,"Food","Breakfast",'20-09-2024')
myTracker.addExpense(500,"Clothes","Bought a T-shirt",'22-09-2024')
myTracker.addExpense(1000,"Travel","Tour to Bandarban",'28-09-2024')
myTracker.addExpense(4000,"Travel","A tour to Switzerland",'02-10-2024')

myTracker.viewExpenses()
myTracker.getTotalExpenses()
myTracker.generateReport()