# -*- coding: utf-8 -*-

# %%
from pulp import *

# define variables
x_sa = LpVariable("x_sa", 0, 5)
x_sb = LpVariable("x_sb", 0, 3)
x_sc = LpVariable("x_sc", 0, 13)
x_ad = LpVariable("x_ad", 0, 3)
x_be = LpVariable("x_be", 0, 4)
x_ca = LpVariable("x_ca", 0, 7)
x_cb = LpVariable("x_cb", 0, 5)
x_cd = LpVariable("x_cd", 0, 2)
x_ce = LpVariable("x_ce", 0, 2)
x_dt = LpVariable("x_dt", 0, 5)
x_ed = LpVariable("x_ed", 0, 9)
x_et = LpVariable("x_et", 0, 10)
f = LpVariable("f", 0)

# define the problem
prob = LpProblem("max_flow", LpMaximize)

# define constraints
# Ix Ax <= b
prob += f - x_sa - x_sb - x_sc == 0
prob += x_ad - x_sa - x_ca == 0
prob += x_be - x_sb - x_cb == 0
prob += x_ca + x_cb + x_cd + x_ce - x_sc == 0
prob += x_dt - x_ad - x_cd - x_ed == 0
prob += x_ed + x_et - x_be - x_ce == 0
prob += f - x_dt - x_et == 0

# define function to maximise
prob += f, "Objective function"

# %% solve the problem
prob.solve()

# access the results
print value(f)
 
