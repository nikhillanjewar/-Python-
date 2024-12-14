# Display Powers of 2 Using Anonymous Function -Lambda Function

nterms = int(input("Enter a Number of terms here:"))
result = list(map(lambda x : 2**x, range(nterms+1)))

print(result)
for i in range(nterms +1):
    print("The Value of 2 raised to power ", i, "is", result[i])

