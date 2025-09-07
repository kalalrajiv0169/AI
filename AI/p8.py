def objective_function(x):
    return -x**2 + 4*x

x = 0
step = 0.1
max_iterations = 100

for _ in range(max_iterations):
    new_x = x + step
    if objective_function(new_x) > objective_function(x):
        x = new_x
    else:
        break

print("Maximum value is at x =", round(x, 2), "with f(x) =", round(objective_function(x), 2))
