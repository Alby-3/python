
"""Write program:
Take 5 numbers from user
Store them in a list using:
append()
Print the list
Rules
Must use:
empty list
loop
append()
input()
Write full code."""""
print("Enter 5 numbers")
lists=[]
for i in range(5):
    num=int(input())
    lists.append(num)
print(lists)
