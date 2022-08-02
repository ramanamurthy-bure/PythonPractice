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
            print("Linked list is empty!")
            self.head = Node(data, None)
            return

        itr = self.head
        while itr:
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
    lkdl.insert_at_beginning(23)
    lkdl.insert_at_beginning(33)
    lkdl.insert_at_beginning(43)
    lkdl.display()
