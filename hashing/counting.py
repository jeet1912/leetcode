from collections import defaultdict, Counter

class Counting:
    
    # Find the length of the longest substring that contains at most k distinct characters.
    def longestSubWithKDistinct(self, string, k):
        p = defaultdict(int)
        l = r = ans = 0
        for r in range(len(string)):
            p[string[r]] += 1
            while len(p) > k:
                p[string[l]] -= 1
                if (p[string[l]] == 0):
                    del p[string[l]]
                l +=1
            ans = max(ans,r-l+1)
        return ans

    # Time complexity - O(n), where n is length of strength
    # Space compleity - O(k)

    # Intersection of all arrays 
    # Given a 2D array nums that contains n arrays of distinct integers,
    # return a sorted array containing all the numbers that appear in all n arrays.
    def intersectionOfAllArray(self,nums):
        p = defaultdict(int)
        for arr in nums:
            for x in arr:
                p[x] +=1
        n = len(nums)
        ans = []
        for x, count in p.items():
            if count == n:
                ans.append(x)
        return sorted(ans)
    # Time complexity
    # n - number of arrays, m - length of each array
    # to sort, m*log(m) 
    # to create dic, n*m
    # m*n + m*log(m) = m * (n + logm), since every ele is unique, m*n


    # Check if all characters have equal number of occurrences
    def areOccurrancesEqual(self,string):
        p = defaultdict(int)
        for char in string:
            p[char] += 1
        s = set(p.values())
        if len(s) == 1:
            return True
        return False  
    
    # Subarray sums equal to K in O(n) time complexity
    def subArraysWithSumK(self, nums,k):
        p = defaultdict(int)
        p[0] = 1                            #empty sub-array
        curr = ans = 0
        for r in nums:
            curr += r
            ans += p[curr-k]
            p[curr] += 1
        return ans
    
    # Given an array of positive integers nums and an integer k. 
    # Find the number of subarrays with exactly k odd numbers in them. 

    def numberOfNiceSubarrays(self,nums,k):
        p = defaultdict(int)
        p[0] = 1
        curr = ans = 0
        for num in nums:
            curr += num%2
            ans += p[curr-k]
            p[curr] +=1
        return ans
    
    # Find Players With Zero or One Losses
    # Time complexity n*log(n)
    def playersWithZeroOrOneL(self,matches):
        zero_loss = set()
        one_loss = set()
        more_losses = set()
        for winner,loser in matches:
            if (winner not in one_loss) and (winner not in more_losses):
                zero_loss.add(winner)
            if loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)
            elif loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in more_losses:
                continue
            else: 
                one_loss.add(loser)
        return [sorted(list(zero_loss)),sorted(list(one_loss))]
            

    # Return largest unique element
    def largestUniqueElement(self,nums):
        p = defaultdict(int)
        for num in nums:
            p[num] +=1
        result = []
        for key,value in p.items():
            if value == 1 :
                result.append(key)
        if len(result) != 0:
            return max(result)    
        else: 
            return -1
    
    # Max number of baloons 
    # Given a string text, you want to use the characters of text 
    # to form as many instances of the word "balloon" as possible.
    # can use each character in text at most once. 
    # Return the maximum number of instances that can be formed.
    def maxNoBaloons(self,text):
        """    
        b  = text.count('b')
        a  = text.count('a')
        l  = text.count('l')//2
        o  = text.count('o')//2
        n  = text.count('n')        
        return min(b,a,l,o,n)
    """
        p = defaultdict(int)
        for char in text:
            p[char] += 1
        c = ['b','a','l','o','n']
        val = {}
        for char in c:
            if char not in p.keys():
                return 0
            if char == "l" or char == "o":
                val[char] = p[char]//2
                print(p[char]//2)
            else: 
                val[char] = p[char]
        return min(val.values())
    
    def sumOfUniqueElements(self, nums):
        p = defaultdict(int)
        for n in nums:
            p[n] += 1
        sum = 0
        for key,val in p.items():
            if val == 1:
                sum += key   
        return sum
    
    def luckyInteger(self,nums):
        p = Counter(nums)
        ans = []
        for key,value in p.items():
            if key == value:
                ans.append(value)
        if len(ans)>0:
            return max(ans)
        else:
            return -1
    
    def uniqueOccurences(self,nums):
        p = Counter(nums)
        v = p.values()
        set_v = set(v)
        if len(set_v) == len(v):
            return True
        return False
    
    def sortByFrequency(self,s):
        p = Counter(s)
        sorted_p = sorted(p.items(), key=lambda x:x[1],reverse=True)
        ans = []
        for key,value in sorted_p:
            ans.append(key*value)
        return ''.join(ans)

    # n[i] == n[j] for i < j
    def goodPairs(self,nums):
        return sum(k * (k - 1) / 2 for k in Counter(nums).values())

    # Given a binary array nums and an integer goal, 
    # return the number of non-empty subarrays with a sum goal.    
    def numSubArrayWithSum(self,nums):
        pass

c = Counting()
l = c.goodPairs([1])
print(l)
