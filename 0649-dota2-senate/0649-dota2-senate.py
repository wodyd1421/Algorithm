class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        while ('R' in queue) and ('D' in queue):
            if queue[0] == 'R':
                queue.remove('D')
            else:
                queue.remove('R')
            queue.rotate(-1)
        return 'Radiant' if queue[0] == 'R' else 'Dire'