from collections import defaultdict, Counter

class Miscellaneous:
    # Group anagrams from an array of strings
    def anagramStr(self,strs):
        p = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string))
            p[key].append(string)
        ans = list(p.values())
        return ans
    # n strings of length m, iterate over strings -> O(n), sort them O(m.logm) so O(nmlogm),
    # iterating over values -> worst case: O(n) (no anagrams in strs), O(nmlogm)(n)
    # space complexity O(nm) (dictionary)

    # min Consecutive Cards to pick up
    # Given an integer array cards, find the length of the shortest subarray 
    # that contains at least one duplicate. If the array has no duplicates, return -1.
    # same as finding the min distance b/w any two of the same element
    def minCardPickUp(self,nums):
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        
        for key in dic.keys():
            arr = dic[key]
            for i in range(len(arr)-1):
                ans = min(float('inf'),arr[i+1]-arr[i]+1)
        return ans if ans < float('inf') else -1
        
        """
        for worst case O(n) space complexity:
            for i in range(len(nums)):
                if nums[i] in dict:
                    mini = min(float('inf),i-dic[num[i]]+1)
            dic[cards[i]] = i
        return ans if ans < float("inf") else -1
        """

    def get_digit_sum(self,num):
        digit_sum = 0
        while num>0:
            digit_sum += num % 10
            num //=10
        return digit_sum
    
    # Given an array of nums, find max num[i] + num[j]
    # where num[i] and num[j] have the same digit sum
    def getMaxSum(self,nums):
        dic = defaultdict(list)
        for num in nums:
            digit_sum = self.get_digit_sum(num)
            dic[digit_sum].append(num)
        ans = -1
        for key in dic:
            curr = dic[key]
            if len(curr)>1:
                curr.sort(reverse=True)
                ans = max(ans,curr[0] + curr[1])
        return ans
    
    def getMaxSum2(self,nums):
        dic = defaultdict(int)
        ans = -1
        for num in nums:
            digit_sum = self.get_digit_sum(num)
            if digit_sum in dic:
                ans = max(ans, dic[digit_sum] + num)
            dic[digit_sum] = max(dic[digit_sum],num)
        return ans
    
    # Equal row and column pairs
    # Given an n x n matrix grid, return the number of pairs (R, C) 
    # where R is a row and C is a column, and R and C are equal if we consider them as 1D arrays.
    
    def equalPairs(self,nums):
        # idea : store arrays as keys
        def convert_arr_toKey(arr):
            return tuple(arr)

        dic = defaultdict(int)
        for row in nums:
            dic[convert_arr_toKey(row)] += 1

        dic2 = defaultdict(int)
        for col in range(len(nums[0])):
            current_col = []
            for row in range(len(nums)):
                current_col.append(nums[row][col])
            dic2[convert_arr_toKey(current_col)] +=1
        
        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]
                

    # Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
    # by using the letters from magazine and false otherwise.
    # Each letter in magazine can only be used once in ransomNote.
    def ransomFromMag(self,ran,mag):
        r = Counter(ran)
        mag = Counter(mag)
        if r & mag == r:
            return True
        else:
            return False
        
    def numJewelsInStones(self,jewels,stones):
        s = Counter(stones)
        j = 0 
        for char in jewels:
            if char in stones:
                j+= s[char]
        return j

    # Length of longest substring without repeating characters
    def lengthOfLongestSubstring(self,s):
        p = defaultdict(int)
        l = 0
        ans = 0 
        for index, char in enumerate(s):
            if char in p:
                l = max(l, p[char]+1)
            p[char] = index
            ans = max(ans,index-l+1)
        return ans

            
        

        
m = Miscellaneous()
y = m.lengthOfLongestSubstring('abcabc')
print(y)
