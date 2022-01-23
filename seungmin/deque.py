class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_data(self):
        print(self.data)

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        if self.is_empty():
            return 0
        else:
            temp = self.head
            cnt = 1

            while temp != self.tail:
                temp = temp.right
                cnt += 1
            return cnt

    def is_empty(self):
        if self.head is None:
            return 1
        else:
            return 0

    def push_front(self, data):
        temp = Node(data)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            self.head.set_left(temp)
            temp.set_right(self.head)
            self.head = temp

    def push_back(self, data):
        temp = Node(data)
        if self.is_empty():
            self.tail = temp
            self.head = temp
        else:
            self.tail.set_right(temp)
            temp.set_left(self.tail)
            self.tail = temp

    def pop_front(self):
        if self.is_empty():
            print(-1)
        elif len(self) == 1:
            self.head.get_data()
            self.head = None
            self.tail = None
        else:
            self.head.get_data()
            self.head = self.head.right
            self.head.left = None

    def pop_back(self):
        if self.is_empty():
            print(-1)
        elif len(self) == 1:
            self.tail.get_data()
            self.tail = None
            self.head = None
        else:
            self.tail.get_data()
            self.tail = self.tail.left
            self.tail.right = None



if __name__ == "__main__":
    n = int(input())
    deq = Deque()

    for _ in range(n):
        inst = input().split()
        if "push_front" in inst:
            deq.push_front(inst[1])
        elif "push_back" in inst:
            deq.push_back(inst[1])
        elif "pop_front" in inst:
            deq.pop_front()
        elif "pop_back" in inst:
            deq.pop_back()
        elif "size" in inst:
            print(len(deq))
        elif "empty" in inst:
            print(deq.is_empty())
        elif "front" in inst:
            if deq.is_empty():
                print(-1)
            else:
                deq.head.get_data()
        elif "back" in inst:
            if deq.is_empty():
                print(-1)
            else:
                deq.tail.get_data()
            

