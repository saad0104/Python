from expense import Expense


def main():
    print("Running Expense Tracker")
    
    expense_file = "expenses.csv"
    budget = 9000
    
    expense = getInput()
    # print(expense)
    
    
    saveExpense(expense, expense_file)
    
    
    summarizeExpense(expense_file,budget)
    
    
    
def getInput():
    print("Getting User Expense ")
    expensename = input("Enter Expense Name: ")
    print(green(f"You've Entered {expensename}"))
    expenseamount = float(input("Enter Expense Amount: "))
    print(green(f"Youve Entered {expenseamount}"))
   
    expense_categories = [
        "Food" , 
        "Transport" ,
        "Living" ,
        "Others" ,
   ]

    while True:
        print("Select Category: ")
        for i,expense_categorie in enumerate(expense_categories):
            print(f"{i+1}. {expense_categorie}") 
            
        Value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a Category Number {Value_range}")) -1
         
        if selected_index in range (len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name = expensename,category= selected_category , amount = expenseamount)
            return new_expense
        else :
            print("Invalid value Entered")



def saveExpense(expense, expense_file):
    print(f"Saving Expense: {expense} to {expense_file}")
    
    with open(expense_file,'a') as file:
        file.write(f"{expense.name}, {expense.amount} , {expense.category}\n")
        
   

def summarizeExpense(expense_file,budget):
    # print("Summarizing Expense")
    
    all_expenses: list[Expense] = []
    
    with open(expense_file,'r') as file:
        lines = file.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(',')
            line_expense = Expense(name=expense_name, amount= float(expense_amount), category= expense_category)
            # print(line_expense)
            all_expenses.append(line_expense)
            
    # print(all_expenses)
            
    amount_by_cat = {}   
    for expense in all_expenses:
        key = expense.category
        if key in amount_by_cat:
            amount_by_cat[key] += expense.amount
        else:
            amount_by_cat[key] = expense.amount
            
    # print(amount_by_cat) 
    print("Total Expenses by category: ")   
    for key,amount in amount_by_cat.items():
        print(f"{key} : ${amount}")

    
    total_spent = sum([ex.amount for ex in all_expenses])
    print(f"You've Spent Total : ${total_spent}")
    remaining_budget = budget - total_spent
    print(green(f"Budget Remaining : ${remaining_budget}"))
    
 
def green(text):
    return f"\033[92m{text}\033[0m"
   
   
   
if __name__ == "__main__" :
    main()