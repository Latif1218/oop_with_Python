

from typing import List

def remove_Duplicates(num: List[int]):
    if not num:
        return 0
    k = 1
    for i in range(1, len(num)):
        if num[i] != num[i - 1]:
            num[k] = num [i]
            k += 1
    return k


print(
    remove_Duplicates([0,0,1,1,1,2,2,3,3,4])
)













