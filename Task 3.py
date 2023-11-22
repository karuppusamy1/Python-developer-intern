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

    def traverse(self):
        current_node=self.head
        while current_node:
            print(current_node.data,end="")
            current_node=current_node.next

linked_list=LinkedList()
linked_list.append(input("Enter a value:"))
linked_list.append(input("Enter a value:"))
linked_list.append(input("Enter a value:"))

print("Linked List:")
linked_list.traverse()
        
