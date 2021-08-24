class Leetcode:

  def searchInsertPostion(self,nums:[int],target:int) -> int:
    #nums is sorted
    '''
    for i,n in enumerate(nums): 
      if(target == n):
        return i
      elif(target < n and i != len(nums)-1):
        return i
      elif(target > n and i == len(nums)-1):
       return len(nums)
    ''' 
    r = len(nums) - 1
    l = 0
    while l<=r:
      mid = (l + r) // 2
      if(nums[mid]>target):
        r = r - 1
      elif(nums[mid]==target):
        return mid
      else:
        l = l + 1
    return r + 1

  def threeSumZero(self,nums:[int]) -> [[int]]:
    length = len(nums)
    nums.sort()
    uniqueTriplets = []
    for i in range(0,length-2):
      l = i + 1
      r = length - 1
      while l < r:
        x = nums[i]
        if(nums[l] + nums[r] + x == 0):
          newTriplet = [nums[l], nums[r],x]
          if newTriplet not in uniqueTriplets:
            uniqueTriplets.append(newTriplet)
          l += 1
          r -= 1
        elif(nums[l] + nums[r] + x < 0):
          l+=1
        else:
          r-= 1
    return uniqueTriplets

  def calculateMovingAverages(self,x: [int], windowSize: int) -> [int]:
    movingAvg = []
    for i in range(len(x)-windowSize+1):
      avg = 0
      for j in range(i,windowSize+i):
        avg += x[j]
      movingAvg.append(avg/3)
    return movingAvg

  def calculateXpowerY(self,x:[int],y:[int]) -> [int]:
    z = 1
    while y > 0:
      if(y%2==0):
        x = x * x
        y = y - 1
      else:
        z = z * x
        y = y - 1
    return z
  
  def partition(self,start:[int],end:[int],arr:[int]) -> [int]:
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end:
      while start < len(array) and array[start] <= pivot:
        start += 1
              
      while array[end] > pivot:
        end -= 1
          
      if(start < end):
        array[start], array[end] = array[end], array[start]
    
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end

  
  def quicksort(self,start:[int],end:[int],arr:[int]) -> [int]:
    if(start<end):
      p = self.partition(start,end,arr)
      quicksort(start,p-1,arr)
      quicksort(p+1,end,arr)
    return arr

  def mergeSort(self, arr:[int]) -> [int]:
    if(len(arr)>1):
      m = len(arr) // 2
      L = arr[:m]
      print('L',L)
      R = arr[m:]
      print('r',R)
      self.mergeSort(L)
      self.mergeSort(R)
      i = j = k = 0
      while i < len(L) and j < len(R):
        if(L[i] < R[j]):
          arr[k] = L[i]
          i +=1
        else:
          arr[k] = R[j]
          j+=1
        k+=1
      while (i<len(L)):
        arr[k] = L[i]
        k+=1
        i+=1
      while (j<len(R)):
        arr[k] = R[j]
        k+=1
        j+=1
    return arr
        

  def insertionSort(self,arr:[int]) -> [int]:
    for i in range(1,len(arr)):
      key = arr[i]
      j = i - 1
      while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -=1
      arr[j+1] = key
      print(arr)
    return arr

  def bubbleSorted(self,arr:[int]) -> [int]:
    for i in range(len(arr)):
      for j in range(0,len(arr)-i-1):
        if(arr[j]>arr[j+1]):
          arr[j],arr[j+1] = arr[j+1],arr[j]
      print(arr)
    return arr

  def selectionSort(self,arr:[int]) -> [int]:
    for i in range(len(arr)):
      min_idx = i
      for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
          min_idx = j
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
      print(arr)
    return arr
    
  def integerToRoman(self,num: int) -> str:
    conversion = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
    count = {'M':0,'CM':0,'D':0,'CD':0,'C':0,'XC':0,'L':0,'XL':0,'X':0,'IX':0,'V':0,'IV':0,'I': 0}
    for key,val in conversion.items():
      print(key,val)
      if(num<val): continue
      else: 
        count[key] = num // val
        num = num % val
        print(num)
    roman = ''  
    for key,val in count.items():
      roman = roman + key*val
    return roman

  def containerWithMostWater(self,height:[int])-> int:
    """
    maxArea = 0
    for i,h in enumerate(height):
      for j,h1 in enumerate(height,i+1):
        maxArea = max(maxArea,(j-i)*min(h,h1))
        
    ----------------------------------------------------------------naive approach       
    """
    r = len(height) - 1
    l = 0
    maxArea = 0
    while l < r:
      maxArea = max(maxArea,(r-l)*min(height[r],height[l]))
      if(height[r] > height[l]):
        l +=1
      else: r-=1
    print(r,l)
    print(min(height[r],height[l]))
    return maxArea
    

  def removeElement(self,nums: [int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
      if(nums[i]==val):
        continue
      nums[k] = nums[i]
      k = k + 1
    nums = nums[:k]
    print(nums)
    return k

  def removeDuplicates(self,nums:[int]) -> int:
    k = 1
    if(len(nums) == 0 or len(nums) == 1):
      return len(nums)
    for i in range(1,len(nums)):
      if(nums[i-1] == nums[i]):
        continue
      nums[k] = nums[i]
      k = k + 1
    nums = nums[:k]
    print(nums)
    return k

  def validParentheses(self, s:str) -> bool:
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in s:
      if i in open_list:
        stack.append(i)
      elif i in close_list:
        pos = close_list.index(i)
      if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
        stack.pop()
      else:
        return False
      if len(stack) == 0:
        return True
      else:
        return False

  def longestCommonPrefix(self,strs: [str]) -> str:
    if(len(strs) == 1):
      return strs[0]
    shortestString = min(strs,key=len)
    print('Shortest:',shortestString)
    prefixes = []
    for i in range(1,len(shortestString)+1):
      prefixes.append(shortestString[:i])
    print('Prefixes:',prefixes)
    satisfied = []
    for i in range(len(prefixes)):
      f = 0
      for j in range(len(strs)):
        if(strs[j].startswith(prefixes[i])):
          f = f + 1
        else: 
          f = f    
      if f == len(strs): 
        satisfied.append(prefixes[i])
    if len(satisfied) == 0:
      return ''
    return max(satisfied,key=len)
      
    
  
  def romanToInt(self, s: str) -> int:
    conversion = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    integer = 0
    for i,char in enumerate(s):
      if(i == 0): 
        integer = integer + conversion[char]
      elif((char == 'V' or char == 'X') and s[i-1] == 'I'): 
        integer = integer - conversion[s[i-1]] + conversion[char] - conversion['I']
      elif((char == 'L' or char == 'C') and s[i-1] == 'X'): 
        integer = integer - conversion[s[i-1]] + conversion[char] - conversion['X']
      elif((char == 'D' or char == 'M') and s[i-1] == 'C'): 
        integer = integer - conversion[s[i-1]] + conversion[char] - conversion['C']
        print('yo',integer)
        print('yo',conversion[s[i-1]])
        print('yo',conversion[char])
      else : 
        integer = integer + conversion[char]
      print(integer)
    return integer

  def palindromeNum(self, x:int) -> bool:
    if(x<0):return False
    y = self.reverse(x)
    if(x == y): return True

  def reverse(self,x : int) -> int:
    flag = 0
    if x < 0:
      flag = 1
      x = -x
    rev = 0
    i = 0
    while (x > 0) :
      n = (x % 10)
      rev = rev * 10 + n
      x = x // 10 
    if(flag == 1):
      rev = - rev
    if(rev > 2147483647 or rev < -2147483647):
      return 0
    return rev

  def longestPalindrome(self,s: str) -> str:
    s2 = ''
    n = len(s)
    if(len(s) <= 2):
      return s[0]
    maxLength = 1
    for i in range(n):
      for j in range(i,n):
        flag = 1
        for k in range(0,(j-i)//2 + 1):
          if(s[i+k] != s[j-k]):
            flag = 0
          if (flag != 0 and (j - i + 1) > maxLength):
            start = i
            maxLength = j - i + 1
    s2 = s[start:maxLength]
    return s2 

  def medianOfSortedArrays(self,a1: list,a2: list) -> int:
    a3 = a1 + a2
    a3.sort()
    i = len(a3) // 2
    m = 0
    if(len(a3)%2==0):
      m = (a3[i-1] + a3[i] ) / 2.00
    else:
      m = a3[i]
    return m

  def lengthOfLongestSubstring(self,s: str) -> int:
    if(len(s) == 0):
        return 0
    visited = {}
    substr = ''
    start = 0
    for i,char in enumerate(s):
      if(char in visited):
        start = max(start,visited[char]+1)
      if(len(substr) < i - start + 1):
        substr = s[start:i+1]
      visited[char] = i
    return len(substr)

lc = Leetcode()              
#z = lc.lengthOfLongestSubstring(s='abcabcaa')
#z = lc.medianOfSortedArrays(a1=[1,2,3], a2=[4,5,6,7])
#z = lc.longestPalindrome(s='cbbd')
#z = lc.reverse(x=-1234567)
#z = lc.romanToInt('MMMCDXC')
#z = lc.longestCommonPrefix(strs=["reflo","fl",'flower'])
#z = lc.validParentheses(s='((([)))')
#z = lc.removeDuplicates(nums=[0,0,0,1])
#z = lc.removeElement(nums=[0,1,2,2,3,0,4,2],val=2)
#z = lc.containerWithMostWater(height=[1, 5, 4, 3])
#z = lc.integerToRoman(num=58)
#z = lc.selectionSort(arr=[4,2,3,5])
#z = lc.bubbleSorted(arr=[4,3,5,1])
#z = lc.insertionSort(arr=[4,3,5,1])
#z = lc.mergeSort(arr=[4,3,5,1])
#z = lc.calculateMovingAverages(x=[3,4,5,6,7,8,9,10,11,12],windowSize=3)
#z = lc.threeSumZero(nums=[-1,0,1,2,-1,-4])
z = lc.searchInsertPostion(nums = [1,3,5,6], target = 7)
print(z)