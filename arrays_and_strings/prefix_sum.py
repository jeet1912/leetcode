class PrefixSum:
    
    # Given an integer array nums, an array queries where queries[i] = [x, y] and
    #  an integer limit, return a boolean array that represents the answer to each query. 
    # A query is true if the sum of the subarray from x to y is less than limit, or
    #  false otherwise.
    # Time complexity - O(n+m) where n is length of nums and m is length of queries
    def problem1(self,nums,queries,limit):
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        ans = []
        for x,y in queries: 
            sum = prefix_sum[y] - prefix_sum[x] + nums[x]
            ans.append(sum<limit)
        return ans

    # Given an integer array nums, find the number of ways to split the array into two parts 
    # so that the first section has a sum greater than or equal to the sum of
    #  the second section. The second section should have at least one number.
    def numWaysToSplitArray(self,nums):
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        ans = 0
        for r in range(len(nums)-1):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[-1] - prefix_sum[i]
            if left_sum >= right_sum:
                ans+=1
        return ans
    #Time complexity - O(n) - space complexity
    
    # in O(1) - space complexity
    def numWaysToSplitArray2(self,nums):
        ans = total = 0
        total = sum(nums)
        for r in range(len(nums)-1):
            left_sum += nums[r]
            right_sum = total - left_sum
            if left_sum >= right_sum:
                ans +=1

    # running sum
    def runningSum(self,nums):
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        return prefix_sum
    
    # min value of k, i.e, initial value added to get positive step by step sum
    def minKforPositiveSum(self,nums):
        k = 1
        while(True):
            is_valid = True
            total = k
            for i in range(0,len(nums)):
                total += nums[i]
                if(total<1):
                    is_valid = False
                    break
            if(is_valid):
                return k
            else:
                k+=1

                    
                    
ps = PrefixSum()
t = ps.minKforPositiveSum([-3,6,2,5,8,6])
print(t)