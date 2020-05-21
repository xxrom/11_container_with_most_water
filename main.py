from typing import List

class Solution:
    def maxAreaHard(self, height: List[int]) -> int:
      heightMap = list(map(lambda x: { 'val': x[1], 'i': x[0] }, enumerate(height)))

      for item in heightMap:
        print('val %d, i %d' %(item['val'], item['i']))

      print(' --------------------- ')
      heightMap.sort(key=lambda x: x['val'])

      for item in heightMap:
        print('val %d, i %d' %(item['val'], item['i']))

      for index in range(len(heightMap), 0, -1):
        print('index', index)


      # 1 sort by value with indexes
      # 2 split by groups
      # 3 left and right in the same biggest group
      #     then check group
      # 3.1 then move left to next down group
      #       and find there max dist between these groups (?)
      # 3.2 then move left to next lower group
      #       and --/--
      # 3.3 when left in last group => then move right to lower group
      #       and --/--
      # ...
      # 3.4 when right and left in the same group => check and exit


      return 0

    def maxArea(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1

      max = 0

      while (left < right):
        checkSum = min(height[left], height[right]) * (right - left)
        print('l %d/ r %d (%d)' % (left,right, checkSum))

        if checkSum > max:
          max = checkSum

        if height[left + 1] >= height[right - 1]:
          left += 1
        else:
          right -= 1

      return 0

my = Solution()
# n = [1,8,6,2,5,4,8,3,7] # 49
n = [1 ,1, 3 ,1, 3] # 9
ans = my.maxArea(n)
print("ans", ans)