# Problem-3: With a single integer as the input, generate the following until 
# a = x [series of numbers as shown in below examples]
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5
#     5) input a = 5, then output : 1, 3, 5, 7, 9

def series(a: int):
    limit = a if a % 2 != 0 else a - 1
    r = [2 * i + 1 for i in range(limit)]
    s=','.join(map(str, r))
    return s

n=7
for i in range(n+1):
    print(series(i))





            



 