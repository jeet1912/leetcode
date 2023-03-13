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

    #Given a binary array nums and an integer k, 
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

sw = SlidingWindow()
l = sw.practiceProb2(nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],k=3)
print(l)
