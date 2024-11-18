#TASK 1

def groups_of_3(input: list[int]) -> list[list[int]]:
    new_list = []
    remainder_list = []
    lb = 0
    ub = 2
    while ub<=len(input)-1:
        subl = []
        subl.append(input[lb])
        subl.append(input[lb+1])
        subl.append(input[ub])
        new_list.append(subl)
        lb = lb + 3
        ub = ub + 3
    if lb<=len(input)-1:
        for i in range(lb, len(input)):
            remainder_list.append(input[i])
        new_list.append(remainder_list)
    return new_list

#TASK 2 - in file.py
