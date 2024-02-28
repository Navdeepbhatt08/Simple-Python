arr = [1,2,3,4]
for i in arr:
     a = max(arr)
print('Maximum Element - ',a)

arr.append(2)
print('Array After Append - ',arr)

#Removing element from array using remove() method
arr.remove(2)
print('After Remove - ',arr)

len = len(arr)
product = 1
for i in range(len):
    product = product * arr[i]
print("Product of all elements is ",product)

min_val = min(arr)
print('Minimum Element is ', min_val)
