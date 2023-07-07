x=int(input('Enter a Number :'))
sum=0
temp=x
if(int(x)):
    print('This is Integer')
else:
    print('This is Not Integer')
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if x==sum:
    print(x,'is an Armstrong Number')
else:
    print(x,'is not Armstrong Number')
