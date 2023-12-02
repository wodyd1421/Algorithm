class Solution:
    def predictPartyVictory(self, senate: str) -> list:
        queue = deque(senate)
        while len(queue) != 1:
            if 'R' not in queue or 'D' not in queue:
                break
            if queue[0] == 'R':
                queue.remove('D')
            else:
                queue.remove('R')
            queue.rotate(-1)
        return 'Radiant' if queue[0] == 'R' else 'Dire'