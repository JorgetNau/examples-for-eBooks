# Program to calculate a risk factor's rating
# Created for the eBook "Risk Management Strategies"

# 1. Define the variables
probability = 4  # Probability level (e.g., from 1 to 5)
impact = 5       # Impact level (e.g., from 1 to 5)

# 2. Perform the calculation
risk_rating = probability * impact

# 3. Display the result to the user
print("--- Risk Calculator ---")
print(f"Risk probability: {probability}")
print(f"Risk impact: {impact}")
print("----------------------------")
print(f"The total risk rating is: {risk_rating}")

# 4. Interpretation of the result
if risk_rating >= 15:
    print("\nThis is a HIGH priority risk. It requires immediate attention.")
elif risk_rating >= 8:
    print("\nThis is a MEDIUM priority risk. It should be monitored closely.")
else:
    print("\nThis is a LOW priority risk. It does not require immediate action.")