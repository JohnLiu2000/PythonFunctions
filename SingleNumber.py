## running time 52ms
## Java could achieve it much faster with time of 1ms

class Solution():
      def singleNumber(self, nums, n):
            ## This output the number appear single time
            ## Other numbers appear n times
            ## type nums: list[int]

            nums.sort()
            end = len(nums)-1
            num = nums[0]

            for i in range(end):
                  if i*n != end:
                        if nums[i*n] != nums[(i+1)*n-1]:
                              num = nums[i*n]
                              break
                  elif i*n == end:
                        num = nums[i*n]
                        break
                  
            print(num)
            return num



nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
print(nums)

# define a new object
s = Solution()
s.singleNumber(nums,2)
