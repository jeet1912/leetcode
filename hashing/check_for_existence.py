
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
            
            

h = Hashing()
print(h.question2("abba")) 

