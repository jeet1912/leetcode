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

s = SlidingWindow()
print(s.largestSumSubArray([10,5,2,6],k=3))

