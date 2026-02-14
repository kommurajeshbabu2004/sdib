"""Count digits in an integer entered by the user.

Usage examples:
  echo 12345 | python first.py   -> 5 digits
  echo -123 | python first.py    -> 3 digits
  echo 0 | python first.py       -> 1 digits
"""

'''n=int(input())
count=0
while(n>0):
    n=n//10
    count+=1
print(count)'''



'''n = 30
count = [0] * 101
print("Enter marks of 30 students (0 to 100):")
for i in range(n):
    mark = int(input())
    if 0 <= mark <= 100:
        count[mark] += 1
    else:
        print("Invalid mark! Enter value between 0 and 100")
print("\nMarks Frequency:")
for mark in range(101):
    if count[mark] > 0:
        print(f"Marks {mark}: {count[mark]} student(s)")'''


'''def calculate():
    return "Calculation function called"
print(calculate())'''

'''def m1(a):
    print("address of a inside m1:",id(a))
    a=a+1
    print("address of a inside m1 after modification:",id(a))
    print("Value of a inside m1:",a)
x=10
print("address of x inside method:",id(x))
print("Value of x inside method:",x)
m1(x)
print("value of x inside method:",x)'''


'''try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print("total:",(a/b))
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("This block will always execute.")'''

def calculate(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
print(calculate(10, 2))  
print(calculate(10, 0))
print(calculate(10, 'a'))