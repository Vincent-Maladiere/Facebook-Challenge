from typing import List
from collections import deque, Counter
# Write any import statements here


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here

    total_meals = 0
    q_meals = deque(maxlen=K)
    set_meals = set()

    for idx in range(N):

        meal = D[idx]

        if not meal in set_meals:

          set_meals.add(meal)

          if len(q_meals) == K:
            free_meal = q_meals.pop() 
            set_meals.remove(free_meal)

          q_meals.appendleft(meal)

          total_meals += 1

    return total_meals


def _getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:

  # Write your code here

  total_meals = 0
  meal_buffer = deque(maxlen=K) # size K
  for idx in range(N):
    if D[idx] not in meal_buffer:
        total_meals += 1
        meal_buffer.appendleft(D[idx])

  return total_meals
