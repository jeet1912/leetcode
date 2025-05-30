class PrefixSum:
    
    def answerQueries(self, nums: list[int], queries: list[int], limit: int) -> list[bool]:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])
        # Time complexity is O(n)
        result = []
        for query in queries:
            i , j = query
            sum = prefix[j] - prefix[i] + nums[i]
            if sum > limit:
                result.append(False)
            else:
                result.append(True)
        return result
        # Time complexity is O(m)
        # Net time complexity is O(n+m)

    def question2(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[-1])
        print(prefix)
        ans = 0
        for i in range(len(nums)-1):
            left = prefix[i]
            print("left ",left)
            right = prefix[-1] - prefix[i+1] + nums[i+1]
            print("right ",right)
            if left >= right:
                ans += 1
        return ans
        # Time complexity is O(n)
        # Space complexity is O(n)

    def question2b(self, nums: list[int]) -> int:
        count = curr = 0
        total = sum(nums)
        for i in range(len(nums)-1):
            curr += nums[i]
            if curr >= total - curr:
                count += 1
        return count
        # Time complexity is O(n)
        # Space complexity is O(1)

    def minStartValue(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])
        minPre = min(prefix)
        if minPre > 0:
            return 1
        else:
            return -minPre + 1  
        

    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        avg = [-1] * n
        if 2 * k + 1 > n:
            return avg
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        print("prefix ", prefix)
        for i in range(k, n - k):
            print("prefixes ", prefix[i + k + 1], prefix[i - k])
            total = prefix[i + k + 1] - prefix[i - k]
            avg[i] = total // (2 * k + 1)
        return avg

    
ps = PrefixSum()
print(ps.getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3))