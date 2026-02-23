"""
Question Separate Positive and Negative Numbers
Write program:
Input:
Enter 5 numbers
Example input:
10
-5
7
-2
3
Output:
Positive: [10, 7, 3]
Negative: [-5, -2]
Rules
Must use:
loop
append()
if condition
two separate lists"""
numbers=[]
postive=[]
negative=[]
print("Enter 5 numbers ")
for i in range(5):
    numbers.append(int(input()))
for num in numbers:
    if num>0:
        postive.append(num)
    else:
        negative.append(num)
print(postive)
print(negative)
