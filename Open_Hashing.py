class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_details(self):
        current_node = self.head
        if current_node is None:
            print("The List is empty")
            print("Nothing to print here")
            return
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()  # Print a new line after printing the linked list


def hash_function(size, array):
    hash_table = [None] * size
    for num in array:
        hash_value = num % size
        if hash_table[hash_value] is None:
            hash_table[hash_value] = Linked_list()
        hash_table[hash_value].append(num)
    return hash_table

def print_hash_function(hash_table):
    for linked_list in hash_table:
        if linked_list is not None:
            linked_list.print_details()


if __name__ == '__main__':
    size = int(input("Enter the Size of the Hash Table: "))
    array = [int(input(f"Enter digit {i + 1}: ")) for i in range(size)]

    hashed_table = hash_function(size, array)
    print_hash_function(hashed_table)
