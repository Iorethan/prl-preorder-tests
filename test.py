import subprocess
import sys
import random
import string

cnt = 0
okcnt = 0


def comp(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

def preorder(tree):
    n = len(tree)
    visits = [0] * n
    pre = ""
    position = 0
    while True:
        if visits[position] == 0:
            pre += tree[position]
        visits[position] += 1
        position = next(n, position, visits[position])
        if visits[0] == 3:
            return pre

def next(n, position, visits):
    p = (position - 1) // 2
    l = 2 * position + 1
    r = l + 1
    if visits == 1:
        if l < n:
            return l
    if visits == 2:
        if r < n:
            return r
    return p


for i in range(1, 20):
    tree = ''.join(random.choices(string.ascii_uppercase + string.digits, k=i))
    out = subprocess.check_output(["./test.sh", tree]).decode('utf-8').split("\n")[:-1][0]
    pre = preorder(tree)
    res = comp(pre, out)

    cnt += 1
    if res:
        print(str(i) + " OK")
        okcnt += 1
    else:
        print(str(i) + " FAIL")
        print("-----Original Input-----")
        print(tree)
        print("-----Expected Output----")
        print(preorder)
        print("-------Your Output------")
        print(out)
        
print("Score: " + str(okcnt) + "/" + str(cnt))
if okcnt == cnt:
    print("Well done!")
else:
    print("Some tests are failing!")
