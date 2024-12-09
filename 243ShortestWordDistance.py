class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        firstwordpoc = []
        secwordpoc = []
        output = []

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                firstwordpoc.append(i)
            if wordsDict[i] == word2:
                secwordpoc.append(i) 
        for i in firstwordpoc:
            for j in secwordpoc:
                output.append(abs(i-j))  
        return min(output)                           
