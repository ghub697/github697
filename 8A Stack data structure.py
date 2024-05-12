def create_stack():
    stack=[]
    return stack

def check_empty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print("pushed item: " + item)

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()

def selectOption(ch):
    if ch==1:
        x=int(input("Enter the value for push: "))
        push(stack,str(x))
    else:
        print("poped item: " + pop(stack))

stack=create_stack()
ch=0
while (ch<3):
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    ch=int(input("Enter your choice: "))
    selectOption(ch)
    print("stack after popping an element:" +str(stack))

print()