class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        n = Node(None, data, None)
        if self.start is None:
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end="->")
            temp = temp.next
        print("None")

    def print_reverse(self):
        if self.start is None:
            print("List is empty")
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        while temp is not None:
            print(temp.item, end="->")
            temp = temp.prev
        print("None")

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            return
        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.start = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                break
            temp = temp.next

    def count_nodes(self):
        count = 0
        temp = self.start
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def __iter__(self):
        return DLLITERATOR(self.start)

class DLLITERATOR:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# ✅ Example usage
mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10), 15)

for x in mylist:
    print(x, end="->")
print("None")

print("Reverse order:")
mylist.print_reverse()

print("Total nodes:", mylist.count_nodes())
