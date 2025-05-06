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
    
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = defaultdict(int)
        for num in arr:
            d[num] += 1
        pH = set()
        for value in d.values():
            pH.add(value)
        
        if len(pH) != len(d):
            return False
        return True

    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)        
        for char in s:
            d[char] += 1
        sortedD = sorted(d.items(),key= lambda item: item[1], reverse=True)
        ans = []
        for char, count in sortedD:
            for _ in range(count):
                ans.append("".join(char))
        return "".join(ans)
        
    
    def frequencySort2(self, s: str) -> str:
        d = defaultdict(int)
        for char in s:
           d[char] += 1
        pH = set()
        for value in d.values():
            pH.add(value)
        pH = sorted(list(pH), reverse=True)
        finalString = ""
        for val in pH:
           print("val ", val)
           for key, value in d.items():
               print("key and value ", key, value)
               if val == value:
                    for _ in range(value):
                        finalString += "".join(key)
                    print(finalString)
        return finalString
    
    def lengthOfLongestGoodArray(self, nums:list[int], k: int) -> int:
        d = defaultdict(int)
        ans = 0
        left = right = 0
        for right in range(len(nums)):
            d[nums[right]] += 1
            while d[nums[right]] > k:
                d[nums[left]] -=1
                left+=1
            ans = max(ans, right-left+1)
        return ans

    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i<j and nums[i] == nums[j]:
                    count += 1
        return count
    
    def numIdenticalPairs2(self, nums: list[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        pairs = 0
        for num in nums:
            if d[num]!=0:
                d[num]-=1
                pairs+=d[num]
        return pairs
    
    def binarySubArraysWithSumG(sellf, nums:list[int], goal:int) -> int:
        d = defaultdict(int)
        d[0] = 1
        curr = ans = 0
        for right in range(len(nums)):
            curr += nums[right]
            ans += d[curr-goal]
            d[curr] += 1
        return ans
    
    def maxUniqueSubarray(self, nums: list[int]) -> int:
        d = defaultdict(int)
        left = right = ans = 0
        
        prefixSum = [0]*(len(nums)+1)
        
        for i in range(len(nums)):
            prefixSum[i+1] = prefixSum[i] + nums[i]

        for right in range(len(nums)):
            d[nums[right]] += 1
            while d[nums[right]] > 1:
                d[nums[left]] -= 1
                left += 1
            ans = max(ans, prefixSum[right+1] - prefixSum[left])
        return ans
    
    def checkInclusion(self, s1:str, s2:str) -> bool:
        if len(s1)>len(s2):
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(s1)):
            d1[s1[i]] += 1
            d2[s2[i]] += 1
        if d1 == d2:
            return True    
        left = 0
        for right in range(len(s1),len(s2)):
            d2[s2[right]] += 1
            d2[s2[left]] -=1
            if d2[s2[left]] == 0:
                del d2[s2[left]]
            left+=1
            if d1 == d2:
                return True
        return False


c = Counting()
print(c.checkInclusion(s1="ab",s2="eidbaooo"))
