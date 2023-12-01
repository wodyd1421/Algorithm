class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        i = 0
        while True:
            if len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                if -stack[-1]/stack[-2] < 1:
                    del stack[-1]
                elif -stack[-1]/stack[-2] == 1:
                    del stack[-1]
                    del stack[-1]
                else:
                    del stack[-2]
            else:
                if i == len(asteroids):
                    return stack
                stack.append(asteroids[i])
                i += 1
        return stack