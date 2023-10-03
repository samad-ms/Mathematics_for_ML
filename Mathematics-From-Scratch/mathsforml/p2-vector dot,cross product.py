# Define two vectors as lists
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Calculate the dot product
dot_product = sum([x * y for x, y in zip(vector1, vector2)])

# Calculate the cross product
cross_product = [
    vector1[1] * vector2[2] - vector1[2] * vector2[1],
    vector1[2] * vector2[0] - vector1[0] * vector2[2],
    vector1[0] * vector2[1] - vector1[1] * vector2[0]
]

# Print the results
print("Dot Product:", dot_product)
print("Cross Product:", cross_product)

print("--------------------------------------------------")

print(sum([x*y for x,y in zip(vector1,vector2)]))
cross_product=[
    vector1[1]*vector2[2]-vector1[2]*vector2[1],
    vector1[0]*vector2[2]-vector1[2]*vector2[0],
    vector1[0]*vector2[1]-vector1[1]*vector2[0],
]
print(cross_product)
projection = [(dot_product / sum([x ** 2 for x in vector2])) * x for x in vector2]

print("proj",projection)