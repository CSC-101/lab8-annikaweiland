import sys
from typing import Optional


#TASK 2
#sys.argv[1] = ipt
def str_to_float(input: str) -> Optional[float]:
    try:
        floaty = float(input)
        return floaty
    except ValueError as e:
        return e

def sum_of_lines(ipt: str) -> float:
    try:
        fileopen = open(ipt)
        linelist = fileopen.readlines()
    except FileNotFoundError as e:
        return e
    list2 = [i.strip("\n") for i in linelist]
    str = " ".join(list2)
    list3 = str.split()
    floatlist = []
    sums = 0
    for num in list3:
        flt = str_to_float(num)
        if type(flt) == float:
            floatlist.append(flt)
        else:
            print ("cannot convert to float for one of the lines. check text file!")
    for num in floatlist:
        sums +=num
    return sums

if __name__ == '__main__':
    print(sum_of_lines(sys.argv[1]))





