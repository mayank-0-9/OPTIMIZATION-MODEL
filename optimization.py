# Author: mayank sagar 

"""
Business Objective:
A manufacturing company wants to maximize its profit by deciding how many units
of Product A and Product B to produce, based on labor & material constraints.
"""

import pulp

# Define as maximization problem
lp_problem = pulp.LpProblem("Product_Profit_Maximization", pulp.LpMaximize)

# Decision variables (non-negative integers)
x = pulp.LpVariable("Units_of_A", lowBound=0, cat='Integer')
y = pulp.LpVariable("Units_of_B", lowBound=0, cat='Integer')

# Objective: Maximize profit
lp_problem += 20 * x + 30 * y, "Total_Profit"

# Constraints:
# 1. Labor: 2x + 3y ≤ 100 hours
lp_problem += 2 * x + 3 * y <= 100, "Labor_Constraint"
# 2. Material: x + 2y ≤ 80 kg
lp_problem += x + 2 * y <= 80, "Material_Constraint"
# 3. Production limit: x ≤ 40, y ≤ 40
lp_problem += x <= 40, "Max_Product_A"
lp_problem += y <= 40, "Max_Product_B"

# Solve it
lp_problem.solve()

# Print output
print("\n--- Optimization Results ---")
print("Status:", pulp.LpStatus[lp_problem.status])
print("Produce A units:", int(x.varValue))
print("Produce B units:", int(y.varValue))
print("Maximum profit (Rs.):", pulp.value(lp_problem.objective))