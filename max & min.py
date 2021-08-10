array = [1, 2, 3, 4, 10, 100, 8, 4, 2, 0]
temp_array = list(set(array))
mx_array = []
index = 0
for j in range(4):  # 4 because i want 4 maximums from array
    mx = 0
    for i in range(len(temp_array)):  # finding maximum elements
        if temp_array[i] >= mx:
            mx = temp_array[i]
            index = i
    mx_array.append(temp_array.pop(index))
print(mx_array)

# similarly for minimum elements

temp_array = list(set(array))
mn_array = []
index = 0
for j in range(4):  # 4 because i want 4 minimums from array
    mn = 10000000000
    for i in range(len(temp_array)):  # finding minimum elements
        if temp_array[i] <= mn:
            mn = temp_array[i]
            index = i
    mn_array.append(temp_array.pop(index))
print(mn_array)