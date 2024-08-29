# Lists in Python

x = [1,2,3,4,5]
for row in x:
    print(row)
print("**************")
y = [[1,2,3],
     [4,5,6]]
for row in y:
    print(row)
print("**************")

x = [[1,2],
     [3,4]]
z = [list(row)for row in zip(*x)]
print(z)
