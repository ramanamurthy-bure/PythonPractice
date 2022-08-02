class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next= Node(data, None)

    def display(self):
        if self.head is None:
            print("Linked list is empty!")
            return

        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '->'
            itr = itr.next

        print(listr)

    def get_length(self):
        if self.head is None:
            print("Linked list is empty!")
            return 0

        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next

        return counter

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_beginning(data)

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                break

            itr =  itr.next
            counter += 1

    def insert_at(self, index,data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_beginning(data)
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                node = Node(data,itr.next)
                itr.next  = node
                break

            itr =  itr.next
            counter += 1

if __name__ == '__main__':
    lkdl = LinkedList()
    lkdl.insert_at_beginning(1)
    lkdl.insert_at_beginning(2)
    lkdl.insert_at_beginning(3)
    lkdl.insert_at_beginning(4)
    lkdl.insert_at_beginning(5)
    lkdl.display()
    lkdl.remove_at(1)
    print("After removing the element at index 1")
    lkdl.display()
    lkdl.insert_at(2,3)
    print("After inserting 3 at index 2")
    lkdl.display()
    lkdl.insert_values([10,11,12,13,14,15])
    print("After inserting list of data to linkedlist")
    lkdl.display()
    lkdl.insert_at_end(16)
    lkdl.insert_at_end(17)
    lkdl.insert_at_end(18)
    print("After inserting the elements at the end")
    lkdl.display()