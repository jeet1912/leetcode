from collections import defaultdict, Counter

class Miscellaneous:
    
    def returnAnagramsFromArray(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(list)
        for str in strs:
            sortedSt = "".join(sorted(str))
            hashMap[sortedSt].append(str)
        return list(hashMap.values())
    
    def minConsecutiveCardToPick(self, cards: list[int]) -> int:
        seen = {}
        minLen = float('inf')
        for r in range(len(cards)):
            if cards[r] in seen:
                minLen = min(minLen, r - seen[cards[r]] + 1)
            seen[cards[r]] = r
        
        return minLen if minLen!= float('inf') else -1
            
    #def minConsecutiveCardToPick2(self, cards:)
    
m = Miscellaneous()
print(m.minConsecutiveCardToPick(cards=[1,2,6,2,1]))
