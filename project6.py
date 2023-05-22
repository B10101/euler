square = sum(list([i**2 for i in range(1,101)]))
sum_squared = sum(list([i for i in range(1,101)]))

print(square - sum_squared**2)