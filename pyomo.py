from pyomo.environ import *

# Define the optimization model
model = ConcreteModel()

# Define the decision variables
model.x = Var(['chicken', 'lentils'], domain=NonNegativeReals)

# Define the objective function
objective_expr = 31 * model.x['chicken'] + 9 * model.x['lentils']
model.objective = Objective(expr=objective_expr, sense=maximize)

# Define the constraints


def protein_constraint_rule(model):
    return 31 * model.x['chicken'] + 9 * model.x['lentils'] >= 150


def calorie_constraint_rule(model):
    return 239 * model.x['chicken'] + 116 * model.x['lentils'] <= 2000


model.protein_constraint = Constraint(rule=protein_constraint_rule)
model.calorie_constraint = Constraint(rule=calorie_constraint_rule)

# Solve the optimization problem
solver = SolverFactory('glpk')
results = solver.solve(model)

# Print the results
print("Chicken quantity: ", value(model.x['chicken']))
print("Lentils quantity: ", value(model.x['lentils']))
