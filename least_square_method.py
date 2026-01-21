
x = [1, 2, 3, 4, 5, 6, 6]
y = [7, 8, 9, 6, 5, 4, 3]

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)


upperPart = 0
lowerPart = 0

# Compute slope (m)
for i in range(len(x)):
    upperPart += (x[i] - x_mean) * (y[i] - y_mean)
    lowerPart += (x[i] - x_mean) ** 2

m = upperPart / lowerPart

# Compute intercept (b)
b = y_mean - m * x_mean

# Predicted Output function
def _predicted(x_val):
    return m * x_val + b

print("Slope of the Model (m):", m)
print("Intercept of the Model (b):", b)

# Predictions
for xi in x:
    print(f"x={xi}, Predicted ŷ={_predicted(xi):.2f}")
