class VPS:
    def __init__(self, n, list_vps):
        self.stack = []
        self.score = []
        for i in range(n):
            vps = list_vps[i]
            vps = list(vps)
            self.check_vps(vps)
        self.print_score(n, self.score)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def isEmpty(self):
        is_empty = False

        if len(self.stack) == 0:
            is_empty = True
        return is_empty

    def print_score(self, n, score):
        for i in range(n):
            if score[i] == 0:
                print("NO")
            else:
                print("YES")

    def check_vps(self, vps):
        for i in vps:
            if i == '(':
                self.push(i)
            else:
                if self.isEmpty():
                    self.score.append(0)
                else:
                    self.pop()
        if self.isEmpty():
            self.score.append(1)
        else:
            self.score.append(0)

if __name__ == "__main__":
    n = int(input())
    list_vps = [input() for i in range(n)]
    v = VPS(n, list_vps)

