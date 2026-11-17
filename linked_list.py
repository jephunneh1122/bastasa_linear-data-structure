# ASSESSMENT 3.2 - LINKED LIST
# Name: JEPHUNNEH E. BASTASA

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()

    def remove_first(self):
        if self.head is not None:
            removed = self.head.data
            self.head = self.head.next
            return removed


# Create linked list
my_list = LinkedList()

# Add letters
for letter in "BASTASA":
    my_list.add(letter)

print("Linked List:", end=" ")
my_list.display()

# Remove from the beginning
while my_list.head is not None:
    print("Remove:", my_list.remove_first())

print("Linked List is EMPTY.")