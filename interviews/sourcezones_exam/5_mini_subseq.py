def get_seq(nums):
    seq_sum = 0
    others_sum = sum(nums)
    ans = []

    # 排序
    nums.sort(reverse=True)

    for i in range(len(nums)):
        # 分兩類: in sequence 、 not in sequence
        seq_sum += nums[i]
        others_sum -= nums[i]
        ans.append(nums[i])
        # 直到sequence的sum > others的sum
        if seq_sum > others_sum:
            break

    return ans

if __name__ == '__main__':
    # nums = [4,3,10,9,8]
    nums = [4,4,7,6,7]
    # nums = [6]

    print(get_seq(nums))
