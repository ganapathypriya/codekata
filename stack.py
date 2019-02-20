print("STACK IMPLEMENT")
stack=[]
while True:
    print("what you want to perform?\n  1.insert the element,2.remove an element,3.check size of stack,4.emptiness of stack,5.exit")
    d=int(input())
    if d==1:
       print("enter the element you want to insert:")
       l=input()
       stack.append(l)    
       print("elements uin stack are:",stack)
    elif d==2:
         if stack==[]:
            print("empty stack.you cannot delete!!")
         else:
             stack.pop()
             print("element bin stack are:",stack)
    elif d==3:
         print("size of stack is:",len(stack))
        #print(element in stack are:",stack)
    elif d==4:
         if stack==[]:
             print("your stack is empty!!")
         else:
             print("your have",len(stack),"elements in tour stack")
             #print("elements in stack are:",stack)
    elif d==5:
         print("exit")
         break
