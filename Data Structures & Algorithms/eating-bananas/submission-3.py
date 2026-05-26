class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = [3,6,7,11] piles of bananas
        # h = 8 hours to eat all the bananas
        #k = min banana eaten per hour, 4
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k) #round up

            if hours <= h:
                res = min(res, k)
                r = k -1
            else:
                l = k+ 1

        return res
