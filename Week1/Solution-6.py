x=input('Enter a String :')
count=0
for i in x:
    count=count+1
a=x[0:2]+x[count-2:count]
print('Input String ='+x)
print('New String ='+a)
