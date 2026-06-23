from util import can_stack_cubes

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))

    print(can_stack_cubes(cubes))