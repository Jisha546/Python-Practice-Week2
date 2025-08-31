✅ Week 2 - Python Practice Exercises

This repository contains 20 beginner-friendly Python exercises with correct solutions.
These exercises help you practice basic Python concepts like input/output, operators, loops, conditionals, strings, lists, and functions.

📚 Topics Covered

✔ Basic Input & Output
✔ Arithmetic Operations
✔ Conditional Statements (if, elif, else)
✔ Loops (for, while)
✔ Number Operations (Even/Odd, Prime, Factorial, Reverse)
✔ Mathematical Calculations (Sum, Fibonacci, Leap Year)
✔ String Manipulation (Palindrome, Reverse, Vowel Count)
✔ List Operations (Max Value, Remove Duplicates, Sort)
✔ Functions (Simple Calculator)
✔ Conversions (Temperature Converter)

✅ List of Exercises

Print Hello World

Sum of Two Numbers

Area of a Circle

Check Even or Odd

Find the Largest of Three Numbers

Sum of First 10 Natural Numbers

Multiplication Table

Factorial of a Number

Reverse a Number

Check Prime Number

Palindrome Check (String)

Count Vowels in a String

Reverse a String

Find Maximum in a List

Remove Duplicates from a List

Sort a List

Simple Calculator using Functions

Fibonacci Series

Check Leap Year

Temperature Converter (Celsius ↔ Fahrenheit)
### ✅ **1. Print Hello World**

```python
# Program to print Hello World
print("Hello, World!")
```

---

### ✅ **2. Sum of Two Numbers**

```python
# Program to find the sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
```

---

### ✅ **3. Area of a Circle**

```python
# Program to calculate area of a circle
import math
radius = float(input("Enter radius: "))
area = math.pi * radius ** 2
print("Area of circle:", area)
```

---

### ✅ **4. Check Even or Odd**

```python
# Program to check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### ✅ **5. Largest of Three Numbers**

```python
# Program to find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest number is:", max(a, b, c))
```

---

### ✅ **6. Sum of First 10 Natural Numbers**

```python
# Program to find sum of first 10 natural numbers
sum_n = sum(range(1, 11))
print("Sum of first 10 natural numbers:", sum_n)
```

---

### ✅ **7. Multiplication Table**

```python
# Program to print multiplication table of a number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

---

### ✅ **8. Factorial of a Number**

```python
# Program to calculate factorial of a number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)
```

---

### ✅ **9. Reverse a Number**

```python
# Program to reverse a number
num = int(input("Enter a number: "))
reverse_num = int(str(num)[::-1])
print("Reversed Number:", reverse_num)
```

---

### ✅ **10. Check Prime Number**

```python
# Program to check if a number is prime
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
```

---

### ✅ **11. Palindrome Check (String)**

```python
# Program to check if a string is a palindrome
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

### ✅ **12. Count Vowels in a String**

```python
# Program to count vowels in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)
```

---

### ✅ **13. Reverse a String**

```python
# Program to reverse a string
text = input("Enter a string: ")
print("Reversed String:", text[::-1])
```

---

### ✅ **14. Find Maximum in a List**

```python
# Program to find maximum element in a list
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Maximum value:", max(numbers))
```

---

### ✅ **15. Remove Duplicates from a List**

```python
# Program to remove duplicates from a list
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique_numbers = list(set(numbers))
print("List without duplicates:", unique_numbers)
```

---

### ✅ **16. Sort a List**

```python
# Program to sort a list
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
print("Sorted list:", numbers)
```

---

### ✅ **17. Simple Calculator using Functions**

```python
# Simple Calculator using functions
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+,-,*,/): ")

if op == '+':
    print("Result:", add(a, b))
elif op == '-':
    print("Result:", sub(a, b))
elif op == '*':
    print("Result:", mul(a, b))
elif op == '/':
    print("Result:", div(a, b))
else:
    print("Invalid Operation")
```

---

### ✅ **18. Fibonacci Series**

```python
# Program to print Fibonacci series
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

---

### ✅ **19. Check Leap Year**

```python
# Program to check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

---

### ✅ **20. Temperature Converter (Celsius ↔ Fahrenheit)**

```python
# Program to convert temperature between Celsius and Fahrenheit
choice = input("Convert to (C/F): ").upper()
temp = float(input("Enter temperature: "))

if choice == 'C':
    print("Temperature in Celsius:", (temp - 32) * 5/9)
elif choice == 'F':
    print("Temperature in Fahrenheit:", (temp * 9/5) + 32)
else:
    print("Invalid Choice")
```

---

