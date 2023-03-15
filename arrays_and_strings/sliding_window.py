class SlidingWindow:    
    #find the length of longest subarray with a sum less than K
    def find_length(self, nums : list[int], k : int) -> int:
        ans = l = sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum > k:
                sum -= nums[l]
                l += 1
            ans = max(ans,r-l+1)
        return ans

    # Time complexity = O(n)
    # Space complexity = O(1) (only 3 variable used)
    #len = find_length(nums=[3,1,2,7,4,1,1,2,5],k=8)
    #print(len)

    # Given a binary string containing 0s and 1s, 
    # find the length of longest substring containing only 1s,
    # after performing a flip operation
    # OR - reframed as follows:
    # find the length of the longest substring containing atmost one 0.

    def find_length2(self, string: str) -> int:    
        ans = l = cur = 0
        for r in range(len(string)):
            if(string[r] == "0"):
                cur += 1
            while cur > 1:
                if(string[l] == "0"):
                    cur -=1
                l+=1
            ans = max(ans,r-l+1)    
        return ans

        #l = find_length2("111010011")
        #print(l)

    # No. subarray product less than k
    def numsubarrayProducLessThanK(self, nums : list[int], k : int) -> int:
        if k <= 1:
            return 0
        prod = 1
        l = ans = 0
        for r in range(len(nums)):
            prod *= nums[r]
            if prod >= k:
                prod //= nums[l]
                l+=1    
            ans += r-l+1
        return ans 
    
    # Given an integer array nums and an integer k, find the sum of the subarray 
    # with the largest sum whose length is k.    
    # Fixed_Window
    def largest_sum(self, nums : list[int], k : int) -> int:
        ans = curr = l = 0
        for r in range(k):
            curr += nums[r]
        ans = curr
        for l in range(k,len(nums)):
            curr += nums[l] - nums[l-k]
            ans = max(ans,curr) 

    #You are given an integer array nums consisting of n elements, and an integer k.
    #Find a contiguous subarray whose length is equal to k that has the maximum average value 
    # and return this value.

    def practiceProb(self, nums: list[int], k: int) -> float:
        avg = sum = 0
        for i in range(k):
            sum += nums[i]
        avg = sum/k

        for i in range(k,len(nums)):
            sum += nums[i] - nums[i-k]
            avg = max(avg,sum/k)
        return avg

    # Given a binary array nums and an integer k, 
    # return the maximum number of consecutive 1's in the array if you can flip at most k 0's    
    
    def practiceProb2(self, nums: list[int], k:int) -> int:
        l = curr = ans = 0 
        for r in range(len(nums)):
            if(nums[r]==0):
                curr += 1
            while curr>k:
                if(nums[l] == 0):
                    curr -=1
                l+=1
            ans = max(ans, r-l+1)
        return ans
    
    # Given an array of positive integers nums and a positive integer target,
    # return the minimal length of a subarray whose sum is greater than or equal to target.
    # If there is no such subarray, return 0 instead.
    def practiceProb3(self,nums,k):
        min_length = float('inf')
        left = cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            while cur_sum >= k:
                min_length = min(min_length,i-left+1)
                cur_sum -= nums[left]
                left+=1

        return min_length if min_length != float('inf') else 0
    
    # Given a string s and an integer k, 
    # return the maximum number of vowel letters in any substring of s with length k.
    def practiceProb4(self,string,k):
        vowels = {"a","e","i","o","u"}
        count = ans = 0
        for i,val in enumerate(string):
            if val in vowels:
                count += 1
            if i>=k and string[i-k] in vowels:
                count -= 1

            ans = max(count,ans)
        return ans

sw = SlidingWindow()
l = sw.practiceProb4("leetcode",3)
print(l)
