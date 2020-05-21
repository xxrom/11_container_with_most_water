1 1 3 1 3 - value
0 1 2 3 4 - index

1 1 1 3 3 - sorted value
0 1 3 2 4 - indexes

# all possible max variants
max dist between 3 group (len(3) > 1) => 2 - 4 => max value = (4-2) * min(3,3) = 6
max dist between 1 and 3 group = 0 - 4 => max value = (4-0) * min(1,3) = 4
max dist between 1 group = 0 - 3 => max value = (3-0) * min(1,1) = 3

min(3,3) * (max(2,4) - min(2,4)) = 3 * 2 = 6
min(1,3) * ()

min(x.val, y.val) * diff(x.i, y.i)
# x = { val: 1, i: 0 }
# y = { val: 3, i: 4 }
d02 = min(1,3) * (4-0) = 1 * 4 = 4

# find where to move
# x = { val: 2, i: 1 }
# y = { val: 3, i: 2 }
d02 = min(1,3) * (2-0) = 1 * 2 = 2