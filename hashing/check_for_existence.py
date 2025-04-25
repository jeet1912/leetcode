
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
    
    def missingNumber(self, nums: list[int]) -> int:
        l = len(nums)
        for i in range(l+1):
            if i not in nums:
                return i
            
    def countingElement(self, nums: list[int]) -> int:
        l = len(nums)
        count = 0
        for i in range(l):
            if (nums[i] + 1) in nums:
                count +=1
        return count
    
    def containsDuplicate(self, nums: list[int]) -> int:
        return True if len(set(nums)) < len(nums) else False


    def destCity(self, paths: list[list[str]]) -> str:
        sourceCities = {}
        cities = set()
        for path in paths:
            sourceCities[path[0]] = path[1]
            cities.add(path[0])
            cities.add(path[1])
        for city in cities:
            if city not in sourceCities.keys():
                return city

    def isPathCrossing(self, path: str) -> bool:
        directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        visited = {(0, 0)}
        current_point = (0, 0)
        for step in path:
            dx, dy = directions[step]
            current_point = (current_point[0] + dx, current_point[1] + dy)
            if current_point in visited:
                return True
            visited.add(current_point)
        return False


h = Hashing()
print(h.isPathCrossing("NESWW")) 

