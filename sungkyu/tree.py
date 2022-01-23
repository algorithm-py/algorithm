class Tree:
    def __init__(self, root, lch, rch):
        self.root = root
        self.lch = lch
        self.rch = rch


def forward(Tree):
    global ans
    if len(ans) == list_length:
        print(ans)
        ans = ""
        return
    if Tree.lch != '.':
        for i in list2:
            if Tree.lch == i.root:
                ans += i.root
                forward(i)
                return
    elif Tree.rch != '.':
        for i in list2:
            if Tree.rch == i.root:
                ans += i.root
                forward(i)
                return
    else:
        for i in list2:
            if Tree.root == i.lch:
                i.lch = '.'
                forward(i)
                return
            elif Tree.root == i.rch:
                i.rch = '.'
                forward(i)
                return


def mid(Tree):
    global ans
    if Tree.lch != '.':
        for i in list2:
            if Tree.lch == i.root:
                mid(i)
                return
    elif Tree.lch == '.':
        if Tree.rch != '.' and Tree.rch != '*':
            ans += Tree.root
            for i in list2:
                if Tree.rch == i.root:
                    mid(i)
                    return
        elif Tree.rch == '.' or Tree.rch == '*':
            if Tree.rch == '.':
                ans += Tree.root
            if len(ans) == list_length:
                print(ans)
                ans = ""
                return
            for i in list2:
                if i.rch == Tree.root:
                    i.rch = '*'
                    mid(i)
                    return
                elif i.lch == Tree.root:
                    i.lch = '.'
                    mid(i)
                    return


def back(Tree):
    global ans
    if Tree.lch == '.' and Tree.rch == '.':
        ans += Tree.root
        if len(ans) == list_length:
            print(ans)
            ans = ""
        for i in list2:
            if i.lch == Tree.root:
                i.lch = '.'
                back(i)
                break
            elif i.rch == Tree.root:
                i.rch = '.'
                back(i)
                break
    elif Tree.lch != '.':
        for i in list2:
            if Tree.lch == i.root:
                back(i)
                break
    elif Tree.lch == '.' and Tree.rch != '.':
        for i in list2:
            if Tree.rch == i.root:
                back(i)
                break


list = []
ans = ""
list_length = int(input())
for i in range(0, list_length):
    root, lch, rch = input().split()
    temp = Tree(root, lch, rch)
    list.append(temp)

import copy

list2 = copy.deepcopy(list)
ans = "A"
forward(list2[0])

list2 = copy.deepcopy(list)
mid(list2[0])

list2 = copy.deepcopy(list)
back(list2[0])