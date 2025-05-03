from collections import defaultdict, Counter

class Counting:
    
    def lengthOfSubstringWithKdistinctChar(self, s:str, k: int) -> int:
        d = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            d[s[right]] += 1
            while len(d) > k:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left+=1
            ans = max(0,right-left+1)
        return ans

    def intersectionOfArrays(self, nums: list[list[int]]) -> list[int]:
        d = defaultdict(int)
        intersection = []
        for array in nums:
            for x in array:
                d[x] += 1
                if d[x] == len(nums):
                    intersection.append(x)
        return sorted(intersection)
    
    def equalOccurrances(self, s:str) -> bool:
        d = defaultdict(int)
        for char in s:
            d[char] +=1
        frequencies = set(d.values())
        #print("Frequencies ",frequencies)
        return len(frequencies) == 1

    def numberOfSubarraysWithSumK(self, nums: list[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        ans = curr = 0
        for r in range(len(nums)):
            curr += nums[r]
            ans += d[curr-k]    
            d[curr] += 1
        return ans

    def numberOfSubArraysWithKOdd(self, nums:list[int], k:int) -> int:
        d = defaultdict(int)
        d[0] = 1
        ans = curr = 0
        for num in nums:
            curr += num % 2 # (1 - num%2 for even)
            ans += d[curr - k]
            d[curr] +=1
        return ans

    def playersWithZeroOrOneLoss(self, nums: list[list[int]]) -> list[int]:
        lost = defaultdict(int)
        won = defaultdict(int)
        for match in nums:
            winner, loser = match[0], match[1]
            if winner not in lost.keys():
                won[winner] +=1
            if loser in won.keys():
                del won[loser]
            lost[loser] +=1
        requiredLosers = []
        for key, value in lost.items():
            if value <= 1:
                requiredLosers.append(key)
        winners = sorted(won.keys())
        requiredLosers = sorted(requiredLosers)
        return [winners,requiredLosers]

    
    def largestUniqueNumber(self, nums: list[int]) -> int:
        occurrances = defaultdict(int)
        onlyOnce = []
        for num in nums:
            occurrances[num] += 1
        for key, value in occurrances.items():
            if value == 1:
                onlyOnce.append(key)
        if len(onlyOnce) == 0:
            return -1
        largest = 0
        for num in onlyOnce:
            if num > largest:
                largest = num
        return largest
        
    def maxNumberOfBalloon(self, text: str) -> int:
        occurrances = {"b":0, "a": 0, "l": 0, "o":0, "n":0}
        for char in text:
            if char in occurrances.keys():
                occurrances[char] +=1
        occurrances["l"] = occurrances["l"]//2
        occurrances["o"] = occurrances["o"]//2
        return min(occurrances.values())
    
    def maxLengthContiguousSubArrWithEqual0s1s(self, nums: list[int]) -> int:
        d = defaultdict(int)
        d[0] = -1
        count = maxLen = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in d:
                maxLen = max(maxLen, i-d[count])
            else:
                d[count] = i
        return maxLen
    
    def sumOfUnique(self, nums: list[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        sum = 0
        for key, value in d.items():
            if value == 1:
                sum += key
        return sum
    
    def maxFrequencyElements(self, nums:list[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        maxVal = 0
        for key, value in d.items():
            if value > maxVal:
                maxVal = value
        ans = 0
        for key, value in d.items():
            if maxVal == value:
                ans += value
        return ans

    def findLucky(self, nums:list[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num]+=1
        ans=[]
        for key, value in d.items():
            if key == value:
                ans.append(key)
        if len(ans) != 0:
            return max(ans)
        return -1
            
c = Counting()
print(c.findLucky(nums=[1,2,2,3,3,3]))
