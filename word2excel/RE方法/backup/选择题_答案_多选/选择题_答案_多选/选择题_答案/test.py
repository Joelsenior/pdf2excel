X = {'A': 5, 'B': 8, 'C': 11, 'D': 14, 'E': 17, 'F': 20}
y = 'ACD'
list1 = []
list2 = []

for char in y:
    if char in X:
        list1.append(X[char])
    else:
        list2.append(char)

print("list1:", list1)
print("list2:", list2)
