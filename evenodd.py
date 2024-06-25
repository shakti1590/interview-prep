# Find Even and odd numbers from the list using python 
n=[1,2,3,4,5,6]
even_num = []
odd_num = []
for num in n:
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)
print("Even numbers:", even_num)
print("Odd numbers:", odd_num)
