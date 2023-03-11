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



    
sw = SlidingWindow()
l = sw.numsubarrayProducLessThanK(nums=[10,5,2,6],k=100)
print(l)
