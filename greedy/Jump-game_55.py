# This questions is very similar to gas station question.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = [False]*n
        ans[n-1]=True
        for i in range(n-2, -1,-1):
            if nums[i]==0:
                continue
            for j in range(i+1,i+nums[i]+1):
                if ans[j]==True:
                    ans[i]=True
                    break
                

        return ans[0]


#         or 


#         Imagine you have a car, and you have some distance to travel (the length of the array). This car has some amount of gasoline, and as long as it has gasoline, it can keep traveling on this road (the array). Every time we move up one element in the array, we subtract one unit of gasoline. However, every time we find an amount of gasoline that is greater than our current amount, we "gas up" our car by replacing our current amount of gasoline with this new amount. We keep repeating this process until we either run out of gasoline (and return false), or we reach the end with just enough gasoline (or more to spare), in which case we return true.
# Note: We can let our gas tank get to zero as long as we are able to gas up at that immediate location (element in the array) that our car is currently at

#         class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         gas = 0
#         for n in nums:
#             if gas < 0:
#                 return False
#             elif n > gas:
#                 gas = n
#             gas -= 1
            
#         return True
