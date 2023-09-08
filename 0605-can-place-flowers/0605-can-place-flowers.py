class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        length = len(flowerbed)
        if length > 1:
            if (flowerbed[0] == 0) & (flowerbed[1] == 0):
                flowerbed[0] = 1
                cnt += 1
            for idx in range(length):
                if (idx > 0) & (idx < length - 1):
                    if (flowerbed[idx - 1] == 0) & (flowerbed[idx + 1] == 0):
                        if flowerbed[idx] == 0:
                            flowerbed[idx] = 1
                            cnt += 1
            if (flowerbed[length - 2] == 0) & (flowerbed[length - 1] == 0):
                cnt += 1
        else:
            if flowerbed[0] == 0:
                cnt += 1
        return cnt >= n