from typing import List


nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # def twoSum(nums, target):
        dic = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dic.keys():
                # print(dic[target - nums[i]], i)
                return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i
        print("not found")

if __name__=='__main__':
    solution = Solution()
    print(solution.twoSum(nums, target))
