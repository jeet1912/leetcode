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
        #Still O(n) since it iterates over all the indices of the array of length n.
        return minValue if minValue!= float('inf') else -1



    def sumOfDigits(self, num: int) -> int:
        digitSum = 0
        while num>0:
            digitSum += num%10
            num //= 10
        return digitSum
    
    def maxSumOfPairWithEqualSumOfDigits(self, nums:list[int]) -> int:
        d = defaultdict(list)
        for num in nums:
            d[self.sumOfDigits(num=num)].append(num)
        maxValue = 0
        for values in d.values():
            if len(values)>1:
                values = sorted(values)
                maxValue = max(maxValue,values[-1] + values[-2])
        return maxValue if maxValue!=0 else -1
    
    
    def maxSumOfPairWithEqualSumOfDigits2(self, nums:list[int]) -> int:
        d = defaultdict(int)
        ans = -1
        for num in nums:
            digitSum = self.sumOfDigits(num=num)
            if digitSum in d:
                ans = max(ans, num + d[digitSum])
            d[digitSum] = max(d[digitSum],num)
        return ans

m = Miscellaneous()
print(m.maxSumOfPairWithEqualSumOfDigits2(nums=[18,43,36,13,7]))
