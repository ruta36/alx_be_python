income=int(input("enter your monthly income: "))
expenses=int(input("enter your monthly expenses:"))
monthly_savings = income - expenses
annual_interest=0.05
projected_savings = monthly_savings * 12 + ( monthly_savings * 12 * annual_interest)


print(f"your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: {projected_savings}.")
