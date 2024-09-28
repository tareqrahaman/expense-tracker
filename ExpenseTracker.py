import os
import json
width = os.get_terminal_size().columns

class Expense:
    def __init__(self,amount,category,description,date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
    def __str__(self):
        return f"amount: ${self.amount} | category: {self.category} | description: {self.description} | date: {self.date}\n"

class Category:
    def __init__(self,name,budget=None):
        self.name = name
        self.budget = budget
        self.total_spent = 0
    def checkBudget(self, amount):
        if self.budget and (self.total_spent + amount) > self.budget:
            print(f"Warning: Spending exceeds the budget for {self.name}!\n")
        self.total_spent += amount

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
        print("\t---'Expense lists'----")
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
    def saveFile(self,filename):
        try:
            with open(filename,'w') as f:
                expense = [expense.__dict__ for expense in self.expenses]
                json.dump(expense,f)
        except:
            print("Something went wrong! Please try again.")
    def loadFile(self,filename):
        try:
            with open(filename,'r') as f:
                exp_list = json.load(f)
                for exp_dict in exp_list:
                    exp_obj = Expense(**exp_dict)  #unpacking the dictionary
                    self.expenses.append(exp_obj)
        except:
            print("Something went wrong! Please try again.")

#menu function for user interection
def menu():
    myTracker = ExpenseTracker()

    #adding categories with budget manually
    myTracker.addCategory("Food",5000)
    myTracker.addCategory("Travel",3000)
    myTracker.addCategory("Clothes",4000)

    #tracker
    empty = True
    print("__Expense Tracker system__".center(width))

    while True:
        choice = int(input(
            """
    1. Add an Expense
    2. View Expenses
    3. Get total Expenses
    4. Generate Report
    5. Save Expenses (json)
    6. Load Expenses (json)
    7. Exit
    Choose an option: """))

        if choice == 1:
            amount = int(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            date = input("Enter the date: ")
            myTracker.addExpense(amount,category,description,date)
            print("Expense added.")
            empty = False
        elif choice == 2:
            if empty: 
                print("No expense Added. Please add an Expense.")
            else:
                myTracker.viewExpenses()
        elif choice == 3:
            myTracker.getTotalExpenses()
        elif choice == 4:
            if empty: 
                print("No expense Added. Please add an Expense.")
            else:
                myTracker.generateReport()
        elif choice == 5:
            filename = input("Enter a file name(.json): ")
            myTracker.saveFile(filename)
            print("File saved successfully.")
        elif choice == 6:
            filename = input("Enter a file name(.json): ")
            myTracker.loadFile(filename)
            print("File loaded successfully.")
        elif choice == 7:
            break
        else:
            print("Invalid option! Please try again.")



    

if __name__ == "__main__":
    menu()

    # ____Manual_for_Testing_____
    # #creating object
    # myTracker = ExpenseTracker()

    # #adding caStegories
    # myTracker.addCategory("Food",5000)
    # myTracker.addCategory("Travel",3000)
    # myTracker.addCategory("Clothes",4000)

    # #adding expenses
    # myTracker.addExpense(100,"Food","Breakfast",'20-09-2024')
    # myTracker.addExpense(500,"Clothes","Bought a T-shirt",'22-09-2024')
    # myTracker.addExpense(1000,"Travel","Tour to Bandarban",'28-09-2024')
    # myTracker.addExpense(4000,"Travel","A tour to Switzerland",'02-10-2024')

    # # myTracker.viewExpenses()
    # # myTracker.getTotalExpenses()
    # # myTracker.generateReport()


    # myTracker.loadFile('manual.json')
    # myTracker.saveFile('data.json')