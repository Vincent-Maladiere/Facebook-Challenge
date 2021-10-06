
import numpy as np


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int, v: bool = False) -> int:
    
    if v:
        print("\n")
        print("="*8)
        print(C)
        print(f"X: {X}, Y: {Y}")

    total = 0
    
    l = np.array(list(C))
    
    if v:
        print(l)
    
    p_pos = np.where(l == "P")[0]

    a_arrays = []
    for p in p_pos:
        a_arrays.append((p+X, p+Y+1))
    
    if v:
        print(a_arrays)

    for a_l, a_r in a_arrays:
        arr = l[a_l:a_r]
        a_pos = np.where(arr == "A")[0]
        for a in a_pos:
            l_edge = a_l+a+X
            r_edge = a_l+a+Y+1
            b_array = l[l_edge:r_edge]
            if v:
                print("  ", b_array)
            total += sum(b_array == "B")
    
    if v:
        print(f"total: {total}")
        print("---")
    
    a_arrays = []
    for p in p_pos[::-1]:
        l_edge = max(p-Y, 0)
        r_edge = max(p-X+1, 0)
        a_arrays.append((l_edge, r_edge))
        
    if v:
        print(a_arrays)
    
    for a_l, a_r in a_arrays:
        m = len(arr)
        arr = l[a_l:a_r]
        a_pos = np.where(arr == "A")[0]
        for a in a_pos:
            l_edge = max(a_l+a-Y, 0)
            r_edge = max(a_l+a-X+1, 0)
            b_array = l[l_edge:r_edge]
            if v:
                print("  ", b_array)
            total += sum(b_array == "B")
    if v:
        print(f"total: {total}")
    return total

def __getArtisticPhotographCount(N: int, C: str, X: int, Y: int, v: bool = False) -> int:
    
    if v:
        print("\n")
        print("="*8)
        print(C)
        print(f"X: {X}, Y: {Y}")

    total = 0
    
    l = np.array(list(C))
    
    if v:
        print(l)
    
    p_pos = np.where(l == "P")[0]

    arrays = []
    for p in p_pos:
        arrays.append(l[p+X:p+2*Y+1])
    
    if v:
        print(arrays)

    for arr in arrays:
        a_pos = np.where(arr == "A")[0]
        a_pos = a_pos[(X-1 <= a_pos) & (a_pos <= Y-1)]
        for a in a_pos:
            l_edge = a+X
            r_edge = a+Y+1
            sub_array = arr[l_edge:r_edge]
            if v:
                print("  ", sub_array)
            total += sum(sub_array == "B")
    
    if v:
        print(f"total: {total}")
        print("---")
    
    arrays = []
    #import ipdb; ipdb.set_trace()
    for p in p_pos[::-1]:
        l_edge = max(p-2*Y-1, 0)
        r_edge = max(p-X+1, 0)
        arrays.append(l[l_edge:r_edge])
        
    if v:
        print(arrays)
    
    for arr in arrays:
        m = len(arr)
        a_pos = np.where(arr == "A")[0]
        a_pos = a_pos[(m-Y <= a_pos) & (a_pos <= m-X)]
        for a in a_pos:
            l_edge = max(a-Y-1, 0)
            r_edge = max(a-X+1, 0)
            sub_array = arr[l_edge:r_edge]
            if v:
                print("  ", sub_array)
            total += sum(sub_array == "B")
    if v:
        print(f"total: {total}")
    return total


def _getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    
    total = 0
    
    l = np.array(list("C"))
    p_pos = np.where(l == "P")[0]

    arrays = []
    for p in p_pos:
        arrays.append(l[p+X:p+2*Y+1])

    for arr in arrays:
        a_pos = np.where(arr == "A")[0]
        for a in a_pos:
            sub_array = arr[a+X:a+Y+1]
            total += sum(sub_array == "B")
            
    arrays = []
    for p in p_pos[::-1]:
        arrays.append(l[p-2*Y-1:p-X])
        
    for arr in arrays:
        a_pos = np.where(arr == "A")[0]
        for a in a_pos:
            sub_array = arr[a-Y-1:a-X]
            total += sum(sub_array == "B")
    
    return total