x = 121
temp=x
rev=0
while(x>0):
    dig=x%10
    rev=rev*10+dig
    x=x//10
print(rev)
if(temp==rev):
    print("True")
else:
    print("False")