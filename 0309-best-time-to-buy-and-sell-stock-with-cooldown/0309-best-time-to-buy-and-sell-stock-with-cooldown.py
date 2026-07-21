from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(day , holding):
            if day >= n :
                return 0 

            if holding == 0 :
                buy = -prices[day] + dfs(day+1 , 1)
                skip = dfs(day + 1 , 0)
                return max(buy ,skip)

            else:
                sell = prices[day] + dfs(day + 2 , 0 )
                hold = dfs( day + 1 , 1)

                return max(sell  , hold)

        return dfs(0, 0)
        