oldstr=input('Enter Any String :')
char=input('Enter a character to replace all vowal with it :')
newstr=''
for i in range(len(oldstr)):
    if oldstr[i]=='a' or oldstr[i]=='A' or oldstr[i]=='e' or oldstr[i]=='E' or oldstr[i]=='i' or oldstr[i]=='I' or oldstr[i]=='o' or oldstr[i]=='O' or oldstr[i]=='u' or oldstr[i]=='U' :
        newstr=newstr+char
    else:
        newstr=newstr+oldstr[i]

print('\nOriginal String :',oldstr)
print('\nNew String :',newstr)
