class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        output = numBottles
        emptybottles = numBottles

        while emptybottles >= numExchange:
            numBottles = emptybottles // numExchange
            output += numBottles
            emptybottles = numBottles + emptybottles % numExchange

        return output    
