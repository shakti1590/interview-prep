# find duplicate element from list using python

a = [1,2,2,3,5,5,7,8,9,9,0,0]
for i in range (0, len(a)):
    for j in range (i+1, len(a)):
        if (a[i] == a[j]):
            print(a[j])
