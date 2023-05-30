class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        sorted_piles = sorted(piles)

        chances = len(piles) // 3

        max_coins = 0

        for i in range(chances):
            
            max_coins += sorted_piles[-2-2*i]

        return max_coins