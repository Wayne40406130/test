numRows=5
res = [[1]]
for i in range(1, numRows):
    print(res[-1]+ [0] )
    res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
    print(res)

