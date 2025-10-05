
# 875. Koko Eating Bananas
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)

        res = right
        
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res

if __name__ == "__main__":
    sol = Solution()
    piles = [3,6,7,11]
    h = 8

    print("Output is : ", sol.minEatingSpeed(piles,h))
    
    piles2 = [30,11,23,4,20]
    h2 = 5

    print("Output is : ", sol.minEatingSpeed(piles2,h2))

