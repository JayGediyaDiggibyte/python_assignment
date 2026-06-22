from util import floor_ceil_rint

values = input().split()
floor_arr, ceil_arr, rint_arr = floor_ceil_rint(values)
print(floor_arr)
print(ceil_arr)
print(rint_arr)