# Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]

#   input: [1,2,8,9,12,46,76,82,15,20,30]
#   Output: 
#     {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

def count_num(n):
    multi= {i: 0 for i in range(1, 10)}

    for num in n:
        for i in range(1, 10):
            if num % i == 0:
                multi[i] += 1
    
    return multi

input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output_dict = count_num(input_list)
print(output_dict)