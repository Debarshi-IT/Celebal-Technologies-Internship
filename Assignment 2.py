class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be greater than 0.")

        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")

        print(f"Deleting node at position {n} with value {current.data}")
        prev.next = current.next

if __name__ == "__main__":
    ll = LinkedList()
    
    print("Adding elements:")
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    ll.print_list()

    print("\nDeleting 3rd node:")
    try:
        ll.delete_nth_node(3)
    except Exception as e:
        print("Error:", e)
    ll.print_list()

    print("\nTrying to delete node at position 10 (out of range):")
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)

    print("\nDeleting all nodes one by one:")
    try:
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)
    ll.print_list()
