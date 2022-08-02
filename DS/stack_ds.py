# Stack is linear data structure implemented in last in first out(LIFO) manner
# We use lists in python to implement the stack data structure
Stack = []


def Push(stk, itm):
    stk.append(itm)


def Pop(stk):
    if stk == []:
        return "Underflow"
    else:
        itm = stk.pop()
        print("------------------------------")
        print("Deleted Item-> :", itm)
        print("------------------------------")
        return itm


def Peek(stk):
    if stk == []:
        print("------------------------------")
        return print("Underflow")
    else:
        print("------------------------------")
        return print(stk[0])


def isEmpty(stk):
    if stk == []:
        print("------------------------------")
        print("Stack is Empty")
        print("------------------------------")
        return True
    else:
        print("------------------------------")
        print("Stack is Not Empty")
        print("------------------------------")
        return False


def Display(stk):
    if stk == []:
        print("------------------------------")
        print("Stack is empty")
        print("------------------------------")
    else:
        print("------------------------------")
        for x in stk:
            print(x)
        print("------------------------------")


while True:
    print("Stack Operations")
    print("1.Push")  # To insert data in the Stack. We can add data only on to the top
    # Overflow : Occurs when stack is full and you are trying to add
    # This occurs only when the stack is fixed size
    print("2.Pop")  # To delete the item from the top of the Stack
    # Underflow : Occurs when stack is empty and you try to pop
    print("3.Peek")  # To inspect the item at the top of the Stack
    print("4.isEmpty")  # To check Stack is empty or not
    print("5.Display")  # To display the Stack elements
    print("6.Exit")  # To exit the Stack operation
    ch = int(input("Enter your choice(1-6) : "))

    if ch == 1:
        item = int(input("Enter Item Val: "))
        Push(Stack, item)

    elif ch == 2:
        Pop(Stack)

    elif ch == 3:
        Peek(Stack)

    elif ch == 4:
        isEmpty(Stack)

    elif ch == 5:
        Display(Stack)

    elif ch == 6:
        break

    else:
        print("Invalid choice!")
        break
