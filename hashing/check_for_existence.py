from collections import Counter
class Hashing:
    def two_sum(self,nums,k):
        p = dict()
        for i,val in enumerate(nums):
            sum = val
            right = k - sum
            if right in p:
                return [i,p[right]]
            p[val] = i   #storing indexes
        return [-1,1]
    
    def firstLetterToAppearTwice(self,string):
        p = set()
        for i,val in enumerate(string):
            if val in p:
                return val
            p.add(val)
        return None
    # space complexity O(m) - m is string length
    # Time complexity O(m)

    # Given an integer array nums, find all the numbers x that satisfy the following:
    # x + 1 is not in nums, and x - 1 is not in nums.
    def practiceProb(self,nums):
        ans = []
        nums = set(nums)
        for num in nums:
            #by converting to set beforehand, these checks are O(1).
            if (((num + 1) not in nums) and ((num - 1) not in nums)): 
                ans.append(num)
        return ans
    
    # Panagram is a sentence where every Eng alphabet appears once.
    def isPanagram(self,str):
        alphabet_length = 26
        p = {}
        for i, char in enumerate(str):
            p[char] = i
        if(len(p.keys())>=alphabet_length):
            return True
        return False
    
    # Given an array nums containing n distinct numbers in the range [0, n], 
    # return the only number in the range that is missing from the array.
    def missingNumber(self,nums):
        p = set(nums)
        for i in range(len(nums)+1):
            if i not in p:
                return i
        return None
    
    # Given an integer array arr, count how many elements x there are, 
    # such that x + 1 is also in arr. 
    # If there are duplicates in arr, count them separately.
    def isXplusOneThere(self, nums):
        c = 0
        for i, val in enumerate(nums):
            if val + 1 in nums:
                c+=1
        return c
    
    # return true if a value appears atleast twice in an array
    def practiceProb1(self,nums):
        p = set()
        for val in nums:
            if val in p:
                return True
            p.add(val)
        return False
    
    def destinationCity(self,paths):
        s = set([p[0] for p in paths])
        for city,dest in paths:
            if dest not in s:
                return dest

    # Given a string path, where path[i] = 'N', 'S', 'E' or 'W',
    # each representing moving one unit north, south, east, or west, respectively. 
    # You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
    # Return true if the path crosses itself at any point, that is,
    # if at any time you are on a location you have previously visited. 
    # Return false otherwise.

    def pathCrossing(self,path):
        x = 0
        y = 0 
        point = [[0,0]]
        for char in path:
            if char == 'N':
                y+=1
            elif char == 'S':
                y-=1
            elif char == 'E':
                x+=1
            else:
                x-=1
            if [x,y] in point:
                return True
            point.append([x,y])
        return False
           
h = Hashing()
o = h.pathCrossing('NWSE')
print(o)
