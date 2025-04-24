
class Hashing:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        t = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in t:
                return t[val], i
            t[nums[i]]=i
    # Time complexity is O(n)
    # Space complexity is O(n)
           
    def question2(self, s: str) -> str:
        t = set()
        s = list(s)
        for char in s:
            if char in t:
                return char
            t.add(char)
        return ""
            
    def question2(self, nums: list[int]) -> set:
        t = set()
        for i in range(license(nums)):
            ele = nums[i]
            l = ele - 1
            r = ele + 1
            if l in nums or r in nums:
                continue
            t.add(ele)
        return t
            
    def pangram(self, s: str) -> bool:
        t = set()
        s = list(s)
        for char in s:
            t.add(char)
        if len(t) == 26:
            return True
        return False
    
    #def missingNumber(self, nums: list[int]) -> int:



h = Hashing()
print(h.pangram("dog")) 

