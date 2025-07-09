from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # Handle collisions
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()      # right asteroid is smaller → remove it
                elif diff > 0:
                    a = 0            # left asteroid is smaller → destroy it
                    break
                else:
                    # same size → both destroy
                    stack.pop()
                    a = 0
                    break

            if a:
                stack.append(a)  # only add if not destroyed

        return stack
