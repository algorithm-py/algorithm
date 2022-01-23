class HanoiTower:
    def __init__(self, num):
        self.cnt = 0
        self.cnt_hanoi(num)
        self.print_cnt()
        self.hanoi(num)
        
    def cnt_hanoi(self, n, start=1, via=2, end=3):
        if n == 1:
            self.cnt_move(start, end)
        else:
            self.cnt_hanoi(n-1, start, end, via)
            self.cnt_move(start, end)
            self.cnt_hanoi(n-1, via, start, end)

    def cnt_move(self, start, end):
        self.cnt += 1

    def hanoi(self, n, start=1, via=2, end=3):
        if n == 1:
            self.move(start, end)
        else:
            self.hanoi(n-1, start, end, via)
            self.move(start, end)
            self.hanoi(n-1, via, start, end)

    def move(self, start, end):
        print("{} {}".format(start, end))

    def print_cnt(self):
        print(self.cnt)

if __name__ == "__main__":
    n = int(input())
    h = HanoiTower(n)

