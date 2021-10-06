from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here

    total_deflated = 0

    for idx in range(N):

        if idx == N-1:
            break

        this_radius = R[-1-idx]
        next_radius = R[max(-2-idx, -N)]

        if this_radius < N-idx:
            return -1

        if this_radius <= next_radius:
            R[-2-idx] = this_radius - 1
            total_deflated += 1

    return total_deflated