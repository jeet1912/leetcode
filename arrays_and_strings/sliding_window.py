class SlidingWindow:

    def question1(self, nums : list[int], k: int) -> tuple[int, list[int]]:
        l = ans = sum = 0
        arr = []
        for i in range(len(nums)):
            sum += nums[i]
            while sum > k:
                sum -= nums[l]
                l += 1
            ans = max(ans, i - l + 1)
            arr = nums[l:i+1]
        return ans, arr
    # Time complexity is O(n)
    # Space complexity is O(1)
    
    def question2(self, nums: list[int]) -> tuple[int, list[int]]:
        l = numZ = ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numZ += 1
            while numZ > 1:
                if nums[l] == 0:
                    numZ -= 1
                l += 1
            ans = max(ans, i - l + 1)
            arr = nums[l:i+1]
        return ans, arr
    # Time complexity is O(n)
    # Space complexity is O(1)

    def numSubArrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        
        l = ans = 0
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            while prod>= k:
                prod //= nums[l]
                l += 1
            ans += r-l+1
        return ans 
    # Time complexity is O(n)
    # Space complexity is O(1)

    def largestSumSubArray(self, nums: list[int], k: int) -> int:
        curr = 0
        for i in range(k):
            curr += nums[i]
        max_sum = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr)
        return max_sum
    
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currSum = currAvg = 0
        for i in range(k):
            currSum += nums[i]
        currAvg = currSum / k
        for i in range(k,len(nums)):
            currSum += nums[i]
            currSum -= nums[i-k]
            currAvg = max(currAvg, currSum / k)
        return currAvg
            
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        numZ = 0 
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numZ += 1
            while numZ > k:
                if nums[l] == 0:
                    numZ -= 1
                l += 1
            ans = max(ans, i-l+1)
        return ans

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        curr = 0
        l = 0
        ans = float('inf')
        for i in range(len(nums)):
            curr+=nums[i]
            while curr >= target:
                ans = min(ans,i-l+1)
                curr -= nums[l]
                l+=1
        if ans == float('inf'):
            return 0
        return ans            

    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        l = 0
        s = list(s)
        count = 0
        maxCount = 0    
        for i in range(k):
            if s[i] in vowels:
                count+=1
        maxCount = max(maxCount,count)
        for r in range(k,len(s)):
            if s[l] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
                maxCount = max(maxCount, count)
            l+=1
        return maxCount
    
s = SlidingWindow()
print(s.maxVowels("abciiidef",k=3))

