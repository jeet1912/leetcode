class PrefixSum:
    
    # Given an integer array nums, an array queries where queries[i] = [x, y] and
    #  an integer limit, return a boolean array that represents the answer to each query. 
    # A query is true if the sum of the subarray from x to y is less than limit, or
    #  false otherwise.
    # Time complexity - O(n+m) where n is length of nums and m is length of queries
    def problem1(nums,queries,limit):
        prefix_sum = nums[0]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        ans = []
        for x,y in queries: 
            sum = prefix_sum[y] - prefix_sum[x] + nums[x]
            ans.append(sum<limit)

    def numWaysToSplitArray():
        pass

ps = PrefixSum()
t = ps.problem1()