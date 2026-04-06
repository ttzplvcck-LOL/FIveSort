from random import randint
import time 

arr = [randint(1, 50) for _ in range(5)] # List of 5 elements  
print(arr)
print("\nBefore" + "---" * 10 + "After")

count = 0
index = 0
start_time = time.time()

min_val = arr[0]  # Find the minimum value in the list  
for x in arr[1:]:  
    if x < min_val:  
        min_val = x

# Swap last two elements if needed  
if arr[-1] < arr[-2]:  
    arr[-2], arr[-1] = arr[-1], arr[-2]
    count += 1 

while True:
    if arr[0] == min_val:
        index = 1

    count += 1
    if arr[index] > arr[-1]:
        temp = arr.pop(index)
        arr.append(temp)
    else:
        temp = arr.pop(index)
        arr.insert(-1, temp)
        if arr[-2] < arr[-3]:  
            arr[-2], arr[-3] = arr[-3], arr[-2]
            count += 1    

    # Check if the list is sorted  
    if arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4]:
        break

end_time = time.time()
print(f"Execution count : {str(count)}   /   Elapsed time : {end_time - start_time:.9f}seconds\n")
print(arr)

# Temp codename: f-king sort ^0^
# Official name: FiveSort (by SeokHee Jung)