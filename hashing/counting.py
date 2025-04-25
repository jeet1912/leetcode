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



c = Counting()
print(c.intersectionOfArrays([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
