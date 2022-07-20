#  n을 입력받아 반복문을 통해 n부터 0까지 출력

import sys

sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(n, -1, -1) :
    print(i, end=' ')