# OPTIMIZATION-MODEL

COMPANY: CODETECH IT SOLUTION

NAME: MAYANK SAGAR

INTERN ID: CT04DN926

DOMAIN: DATA SCIENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

TASK DESCRIPTION:

Objective:

To solve a real-world product mix problem using Linear Programming (LP) to maximize profit under limited resources such as labor and materials.


Problem Scenario:

A company manufactures two products:

Product A gives a profit of Rs. 20 per unit

Product B gives a profit of Rs. 30 per unit


However, they face constraints:

Each unit of Product A uses 2 hours of labor and 1 kg of material

Each unit of Product B uses 3 hours of labor and 2 kg of material

Total labor available: 100 hours

Total material available: 80 kg

No more than 40 units of either product can be produced


The aim is to determine how many units of Product A and Product B should be produced to maximize total profit, without exceeding labor and material constraints.


---

Tools and Libraries:

Python 3: Programming Language

PuLP: Optimization Library used to solve LP problems



---

Step-by-Step Breakdown:

Step 1: Define the Problem

Using the pulp.LpProblem class, we declare a maximization problem. This sets up the framework for profit optimization.

Step 2: Declare Decision Variables

We define two non-negative integer decision variables:

x → Number of units of Product A to produce

y → Number of units of Product B to produce


These variables represent how many units we will produce to maximize profit.

Step 3: Set the Objective Function

The goal is to maximize total profit:

Total_Profit = 20x + 30y

This is added to the LP problem using PuLP’s syntax.

Step 4: Add Constraints

We model three constraints:

Labor Constraint: 2x + 3y ≤ 100

Material Constraint: x + 2y ≤ 80

Production Limits: x ≤ 40 and y ≤ 40


These constraints are essential to ensure that production does not exceed available resources.

Step 5: Solve the LP Problem

Using PuLP’s .solve() method, we solve the LP problem. The solver determines the values of x and y that give maximum profit while satisfying all constraints.

Step 6: Display the Results

We print the following:

Problem status (Optimal or not)

Optimal units to produce for Product A and Product B

Maximum profit achieved


Sample Output:

----- Optimization Results -----
Status: Optimal
Optimal units of Product A to produce: 20
Optimal units of Product B to produce: 20
Maximum profit (Rs.): 1000.0

Conclusion:

This task successfully demonstrates how to build and solve a linear programming model using Python’s PuLP library. We tackled a real-world business scenario involving resource allocation and profit maximization. This kind of optimization task is essential in fields like supply chain, logistics, and operations research.

It builds foundational skills in mathematical modeling and shows how data science can solve core business problems using logic, code, and decision science.
