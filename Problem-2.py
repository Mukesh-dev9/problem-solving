# Problem-2: With a single integer as the input, generate the following 
# until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7
#     5) input a = x, then output : 1, 3, 5, 7, .......
a=7
for i in range(a+1):
    n=[]
    if a>0:
        for j in range(i*2):
            if j%2!=0:
                n.append(j)
        str_num=[str(num) for num in n ]
        print(','.join(str_num))
        n.clear()






  
 
