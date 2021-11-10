class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        i = 1
        while i < len(nums):
            if nums[k] == nums[i]:
                i+=1
            else:
                k+=1
                nums[k] = nums[i]
            
        sub_nums = nums[:k + 1]
        b = sub_nums + ('_ ' * (len(nums) - len(sub_nums))).split()
        print(b)

        return k+1

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]

    sol = Solution()
    print(sol.removeDuplicates(nums))
