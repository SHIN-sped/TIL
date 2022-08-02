import sys
input = sys.stdin.readline

N, M = map(int, input().split())

temp = min(N, M)

print(temp//2)