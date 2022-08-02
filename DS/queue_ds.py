# Queue is linear data structure implemented in first in first out(FIFO) manner
# We use lists in python to implement the queue data structure

Queue = []


def Enqueue(que, itm):
    que.append(itm)


def Dequeue(que):
    if que == []:
        return "Underflow"
    else:
        itm = que.pop(0)
        print("------------------------------")
        print("Item to be popped-> :", itm)
        print("------------------------------")
        return itm


def Peek(que):
    if que == []:
        print("------------------------------")
        return print("Underflow")
    else:
        print("------------------------------")
        return print(que[0])


def isEmpty(que):
    if que == []:
        print("------------------------------")
        print("Queue is Empty")
        print("------------------------------")
        return True
    else:
        print("------------------------------")
        print("Queue is Not Empty")
        print("------------------------------")
        return False


def Display(que):
    if que == []:
        print("------------------------------")
        print("Queue is empty")
        print("------------------------------")
    else:
        print("------------------------------")
        for x in que:
            print(x)
        print("------------------------------")


while True:
    print("Queue Operations")
    print("1.Enqueue")  # To add element to the queue
    print("2.Dequeue")  # To remove element from the queue
    print("3.Peek")  # To inspect the element in queue
    print("4.isEmpty")  # To check queue is empty or not
    print("5.Display")  # To display the queue elements
    print("6.Exit")  # To exit the queue operation
    ch = int(input("Enter your choice(1-6) : "))

    if ch == 1:
        item = int(input("Enter Item Val: "))
        Enqueue(Queue, item)

    elif ch == 2:
        Dequeue(Queue)

    elif ch == 3:
        Peek(Queue)

    elif ch == 4:
        isEmpty(Queue)

    elif ch == 5:
        Display(Queue)

    elif ch == 6:
        break

    else:
        print("Invalid choice!")
        break
