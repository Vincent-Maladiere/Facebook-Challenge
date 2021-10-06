from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:

  has_odd = False
  s_max = 0
  for s in S:
    if s > s_max:
      s_max = s
    if s % 2:
      has_odd = True

  min_pb = s_max // 2 + int(has_odd)

  return min_pb
