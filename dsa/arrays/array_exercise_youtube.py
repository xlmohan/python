expenses_months = ["January", "February", "March", "April", "May"]
expenses_price = [2200, 2350, 2600, 2130, 2000]

for i in range(len(expenses_months)):
    if expenses_months[i] == "March":
        print(f"Expense in March: {expenses_price[i]}")
        break

for i in range(len(expenses_months)):
    for j in range( i > 3 ):
        first_three = expenses_price[j] + expenses_price[j+1] + expenses_price[j+2]
        print(f"Total expense for first three months: {first_three}")

for i in range(len(expenses_price)):
    if expenses_price[i] == 2000:
        output = f"Found an expense of 2000 in month: {expenses_months[i]}"
        print(output)

for i in range(len(expenses_price)):
    expenses_price[i] = expenses_price[i] + 1980
    print(f"Updated expense for {expenses_months[i]}: {expenses_price[i]}")
    
for i in range(len(expenses_months)):
    if expenses_months[i] == "April":
        expenses_price[i] = expenses_price[i] - 200
        print(f"Expense for April after reduction: {expenses_price[i]}")
    print(f"Expense for {expenses_months[i]}: {expenses_price[i]}")
