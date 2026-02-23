"""""write a Python program:
Ask user to enter 5 numbers
Store them in a list using:
append()
Then print the list
Example
Input
10
20
30
40
50
Output:
[10, 20, 30, 40, 50]
Rules
Must use:
empty list
append()
loop
input()"""
lists=[]
print("Enter 5 numbers ")
for i in range(5):
    num=int(input())
    lists.append(num)
print(lists)

