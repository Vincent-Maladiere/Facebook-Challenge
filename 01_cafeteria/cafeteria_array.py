from typing import List
# Write any import statements here
import numpy as np


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  s_mask = initMask(N, K, S)

  s_available = getAvailable(s_mask)
  diners_count = 0
  for s in s_available:
    if s_mask[s] == 0:
      s_mask = fillMask(s, s_mask, N, K)
      diners_count += 1
      
  return diners_count


def initMask(N: int, K: int, S: int) -> np.array:
  
  s_mask = np.zeros(N)
  
  for s in S:
    s_idx = s - 1 
    s_mask = fillMask(s_idx, s_mask, N, K)
  
  return s_mask


def fillMask(s_idx: int, s_mask: np.array, N: int, K: int) -> np.array:
  
  left_s = max(s_idx - K, 0)
  right_s = min(s_idx + K, N)
  s_mask[left_s:right_s+1] = 1
  
  return s_mask


def getAvailable(s_mask: np.array) -> np.array:
  
  s_available = np.where(s_mask == 0)[0]
  
  return s_available
 
  
