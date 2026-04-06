arr = [100, 200, 445, 902, 3]  # Initial list

# Find minimum value
min_val = arr[0]
for x in arr[1:]:
    if x < min_val:
        min_val = x

# Swap last two if needed
if arr[-1] < arr[-2]:
    arr[-2], arr[-1] = arr[-1], arr[-2]

# Main sorting loop
while True:
    if arr[0] == min_val:
        # Handle second element
        if arr[1] > arr[-1]:
            arr.append(arr.pop(1))
        else:
            arr.insert(-1, arr.pop(1))
            if arr[-2] < arr[-3]:
                arr[-2], arr[-3] = arr[-3], arr[-2]
    else:
        # Handle first element
        if arr[0] >= arr[-1]:
            arr.append(arr.pop(0))
        else:
            arr.insert(-1, arr.pop(0))
            if arr[-2] < arr[-3]:
                arr[-2], arr[-3] = arr[-3], arr[-2]

    # Check if sorted
    is_sorted = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_sorted = False
            break

    if is_sorted:
        break

print(arr)  # Sorted list

# Temp codename: f-king sort ^0^
# Official name: FiveSort (by SeokHee Jung)