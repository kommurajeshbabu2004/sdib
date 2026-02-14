'''arr = []
sum_val = 0

for i in range(10):
    num = int(input("Enter number: "))
    arr.append(num)
    sum_val += num

print("Sum of elements:", sum_val)'''



'''arr = []

for i in range(20):
    arr.append(int(input("Enter number: ")))

# Initialize
max1 = max2 = max3 = float('-inf')
min1 = min2 = min3 = float('inf')

for num in arr:
    if num > max1:
        max3, max2, max1 = max2, max1, num
    elif num > max2:
        max3, max2 = max2, num
    elif num > max3:
        max3 = num

    if num < min1:
        min3, min2, min1 = min2, min1, num
    elif num < min2:
        min3, min2 = min2, num
    elif num < min3:
        min3 = num

print("Maximum 3 elements:", max1, max2, max3)
print("Minimum 3 elements:", min1, min2, min3)'''


arr = []

for i in range(10):
    arr.append(int(input("Enter number: ")))

print("Reversed Array:")
for i in range(9, -1, -1):
    print(arr[i], end=" ")


marks_count = [0] * 101

for i in range(30):
    mark = int(input("Enter mark (0-100): "))
    if 0 <= mark <= 100:
        marks_count[mark] += 1

for i in range(101):
    print(f"Marks {i}: {marks_count[i]} students")


ranges = [0] * 10

for i in range(30):
    mark = int(input("Enter mark (0-100): "))
    if 0 <= mark <= 100:
        index = mark // 10
        if index == 10:
            index = 9
        ranges[index] += 1

start = 0
for i in range(10):
    end = start + 9 if i < 9 else 100
    print(f"{start}% to {end}% : {ranges[i]} students")
    start += 10


n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)



