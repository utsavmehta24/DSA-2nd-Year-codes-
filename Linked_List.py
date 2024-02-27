class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_details(self):
        current_node = self.head
        if current_node == None:
            print("The List is empty")
            print("Nothing to print here")
            return
        while current_node:
            print(current_node.data, end = ' ')
            current_node = current_node.next
        
if __name__ == "__main__":
    linked_list = Linked_list()
    
    num = int(input("Enter the Number of elements you want to enter\t"))
    for i in range(num):
        number = int(input(f'Enter the data for {i+1} th node\t'))
        linked_list.append(number)
    
    linked_list.print_details()  