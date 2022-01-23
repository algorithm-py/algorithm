class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.prefix_sum = None
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_data(self):
        print(self.prefix_sum)

class SegmentTree:
    def __init__(self, num_list):
        self.tree = {}
        self.num_list = num_list
        self.build_tree(0, len(num_list)- 1)

    def insert(self, start, end, node):
        prefix = (start, end)
        self.tree[prefix] = node

    def build_tree(self, start, end):
        if start == end:
            self.insert(start, end, Node(start, end))
            temp = self.tree[(start, end)]
            temp.prefix_sum = self.num_list[start]
            return
        self.insert(start, end, Node(start, end))
        temp = self.tree[(start, end)]
        mid = (start + end) // 2
        temp.set_left(Node(start, mid))
        temp.set_right(Node(mid+ 1, end))
        self.build_tree(start, mid)
        self.build_tree(mid+ 1, end)
        temp.prefix_sum = self.tree[(start, mid)].prefix_sum + self.tree[(mid+ 1, end)].prefix_sum
        return

    def modify(self, idx, fixed_num):
        diff = fixed_num - self.num_list[idx]
        root = self.tree[(0, len(self.num_list) -1)]

        while root.start != root.end:
            mid = (root.start + root.end) // 2
            if mid >= idx:
                start, end = root.left.start, root.left.end
                root = self.tree[(start, end)]
                root.prefix_sum += diff
            elif mid +1 <= idx:
                start, end = root.right.start, root.right.end
                root = self.tree[(start, end)]
                root.prefix_sum += diff 

    def query(self, start, end, in_start, in_end):
        if in_start > end or in_end < start:
            return 0

        if in_start <= start and end <= in_end:
            return self.tree[(start, end)].prefix_sum

        mid = (start + end) // 2
        return self.query(start, mid, in_start, in_end) + self.query(mid+ 1, end, in_start, in_end)

if __name__== "__main__":
    n, m, k = map(int, input().split())

    input_list = []

    for _ in range(n):
        temp = int(input())
        input_list.append(temp)

    ans = SegmentTree(input_list)

    for _ in range(m+k):
        a, b, c = map(int, input().split())

        if a == 1:
            ans.modify(b-1, c)
        elif a == 2:
            print(ans.query(0, n-1, b-1, c-1))


