#Create lower triangular, upper triangular and pyramid containing the "*" character.

n = 5  # number of rows

#Lower Triangular

print("Lower Triangular Pattern:")
for i in range(1, n + 1):
    print("* " * i)

#Upper Triangular
    
print("Upper Triangular Pattern:")
for i in range(n, 0, -1):
    print("* " * i)

#Pyramid Pattern
    
print("Pyramid Pattern:")
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
