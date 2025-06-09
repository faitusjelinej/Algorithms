class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0

        for price in prices:
            if price > minprice:
                maxprofit = max(maxprofit, price - minprice)
            else:
                minprice = price

        return maxprofit            
