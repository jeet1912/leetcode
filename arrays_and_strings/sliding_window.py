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

s = SlidingWindow()
print(s.question2([1,1,0,0,1,0,1,1]))