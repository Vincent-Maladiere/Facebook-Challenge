from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> None:

    last_pos = 1
    total_time = 0

    for c in C:
        start = min(last_pos, c)
        end = max(last_pos, c)
        total_time += min(end - start, N - (end - start))
        last_pos = c

    return total_time