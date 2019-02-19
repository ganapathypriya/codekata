b=int(raw_input())
c=b
rev=0
while c!=0:
    rev=(rev*10)+(c%10)
    c=c//10
if b==rev:
    print("yes")
else:
    print("no")
