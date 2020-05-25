from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
      size = len(height)
      heightMap = list(map(lambda x: { 'val': x[1], 'i': x[0] }, enumerate(height)))

      # for item in heightMap:
      #   print('val %d, i %d' %(item['val'], item['i']))

      # print(' --------------------- ')
      heightMap.sort(key=lambda x: x['val'])

      # for item in heightMap:
      #   print('val %d, i %d' %(item['val'], item['i']))

      max = 0
      minVal = -100000

      for i in range(len(heightMap) -1, 0, -1):

        right = heightMap[i]['i']
        rightVal = heightMap[i]['val']
        # check minValue and exit if needs
        if rightVal < minVal:
          print('EXIT!')
          return max

        # print('minVal', minVal)

        # print('N1 %d / val %d / i %d '%(i, heightMap[i]['val'], heightMap[i]['i']))

        for j in range(i-1, -1, -1):
          left = heightMap[j]['i']
          leftVal = heightMap[j]['val']

          # print('  N2 %d / val %d / i %d '%(j, heightMap[j]['val'], heightMap[j]['i']))

          max = self.checkSum(left, right, leftVal, rightVal, max)
          minVal = self.calcMinValue(max, size)

      return max

    def calcMinValue(self, max, arrSize):
      return max / arrSize

    #   # 1 sort by value with indexes
    #   # 2 split by groups
    #   # 3 left and right in the same biggest group
    #   #     then check group
    #   # 3.1 then move left to next down group
    #   #       and find there max dist between these groups (?)
    #   # 3.2 then move left to next lower group
    #   #       and --/--
    #   # 3.3 when left in last group => then move right to lower group
    #   #       and --/--
    #   # ...
    #   # 3.4 when right and left in the same group => check and exit


    #   return 0

    def checkSum(self, left, right, leftVal, rightVal, max):
      checkSum = min(leftVal, rightVal) * abs(right - left)

      if checkSum > max:
        print('     l %d/ r %d (%d)' % (left, right, checkSum))
        print('     >>> new max! %f' %checkSum)
        return checkSum

      return max

    def checkSumOld(self, left, right, height, max):
      checkSum = min(height[left], height[right]) * (right - left)

      if checkSum > max:
        print('     l %d/ r %d (%d)' % (left,right, checkSum))
        print('     >>> new max! %f' %checkSum)
        return checkSum

      return max

    def maxAreaSlow(self, height: List[int]) -> int:
      max = 0
      size = len(height)

      for i in range(0, size):
        left = i
        for j in range(i+1, size):
          right = j
          max = self.checkSumOld(left, right, height, max)

      return max

my = Solution()
n = [1,8,6,2,5,4,8,3,7] # 49
# n = [1 ,1, 3 ,1, 3] # 6
# n = [1,1] # 1
ans = my.maxArea(n)
print("ans", ans)

# TODO: [0 -> 15000] figure out why it is not exit from loop ? ...
# check minVal params

# 8 * 8
# currentMin = 49 / 8 = 7.2
# if val < currentMin => exit - no way to beat this result