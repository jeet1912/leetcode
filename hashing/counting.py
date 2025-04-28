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

        
            
c = Counting()
print(c.numberOfSubarraysWithSumK(nums=[1,1,2,1,1],k=3))
