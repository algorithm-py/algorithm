from sys import stdin, stdout

class node: #기본 노트 클래스
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class tree():
    def __init__(self):
        self.root = None

    def insert(self,in1,in2,in3):
        newrt = node(in1)
        newlf = node(in2)
        newri = node(in3)

        if self.root is None:
            self.root = newrt

        newrt.left = newlf
        newrt.right = newri

    def preorder(self, nd):
        if nd == None:
            pass
        else:
            print(nd.data)
            self.preorder(nd.left)
            self.preorder(nd.right)


n = int(input())
TR = tree()

for i in range(n):
    a, b, c = map(lambda x: None if x == '.' else x, stdin.readline().rstrip().split())
    TR.insert(a,b,c)
TR.preorder(TR.root)

