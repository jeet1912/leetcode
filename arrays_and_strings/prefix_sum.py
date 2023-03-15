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
            left_sum = prefix_sum[r]
            right_sum = prefix_sum[-1] - prefix_sum[r]
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
        return ans

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

    # Given net gain as an array, find the highest altitude
    # max prefix sum
    def highestAltitude(self,nums):
        """
            net_altitude = [0]
            for i in range(0,len(nums)):
                net_altitude.append(nums[i] + net_altitude[-1])
            return max(net_altitude)
        """
        net_altitude = 0
        sol = 0
        for i in nums:
            net_altitude += i
            sol = max(sol,net_altitude)
        return sol

    # Find pivot index
    # The pivot index is the index 
    # where the sum of all the numbers strictly to the left of the index is 
    # equal to the sum of all the numbers strictly to the index's right.
    def findPivotIndex(self,nums):
        right_sum = sum(nums)
        left_sum = 0
        for i, val in enumerate(nums):
            right_sum = right_sum - val
            if left_sum == right_sum : 
                return i
            left_sum += val
        return -1
    
    """
    class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]*(len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i+1] = nums[i] + self.prefix_sum[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]  
    """

ps = PrefixSum()
t = ps.findPivotIndex([1,7,3,6,5,6])
print(t)