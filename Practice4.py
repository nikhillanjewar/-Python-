# SWAP TO VARIABLES 

# WITH USING THIRD VARIABLE
x  = 12
y = 13

# temporary variable
temp = x
x = y
y = temp
print("The value of temp variable is: ", temp)
print("The value of x variable is: ", x)
print("The value of y variable is: ", y)



# WITHOUT USING VARIABLE
a = 13
b = 12
a,b = b,a
print("The value of a:",a)
print("The value of b:",b)