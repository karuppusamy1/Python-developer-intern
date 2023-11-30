class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node

    def find_middle(self):
        slow_pointer=self.head
        fast_pointer=self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next.next

        return slow_pointer.data

linked_list=LinkedList()
linked_list.append(input("Enter a number:"))
linked_list.append(input("Enter a number:"))
linked_list.append(input("Enter a number:"))
linked_list.append(input("Enter a number:"))
linked_list.append(input("Enter a number:"))

middle_element=linked_list.find_middle()
print("The Middle Element is:",middle_element)




