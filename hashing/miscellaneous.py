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
            
    # or length of the shortest subarray        
    def shortestDistanceBetweenDuplicates(self, nums: list[int]) -> int:
        hashMap = defaultdict(list)
        for i, num in enumerate(nums):
            hashMap[num].append(i)
        
        minValue = float('inf')
        for values in hashMap.values():
            for i in range(len(values)-1):
                minValue = min(minValue, values[i+1] - values[i] + 1)
        
        return minValue if minValue!= float('inf') else -1

    
m = Miscellaneous()
print(m.shortestDistanceBetweenDuplicates(nums=[1,2,6,2,1]))
