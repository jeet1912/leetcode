class SlidingWindow:

    def question1(self, nums : list[int], k: int) -> list[int]:
        l = r = ans = sum = 0
        for i in range(nums):
            sum += nums[i]
            while sum > k:
                sum -= nums[l]
                l += 1
            ans = max(ans, i - l + 1)
        return ans
    # Time complexity is O(n)
    # Space complexity is O(1)
    
s = SlidingWindow()
print(s.question1([3,2,1,3,1,1],k=5))