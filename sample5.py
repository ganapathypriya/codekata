Inputvalue=raw_input()
a,b,c=Inputvalue.split(" ")
a,b,c=int(a),int(b),int(c)
if((a>b) and(a>c)):
    print(a)
elif((b>c)and(b>a)):
    print(b)
elif((c>a)and(c>b)):
     print(c)
