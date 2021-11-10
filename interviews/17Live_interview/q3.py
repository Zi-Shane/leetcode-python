    """
Find the minumun positive integer which is not exist in the given array.
    
Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

    """

a = [1,2,0]
sorted(a)

j = 1
for i in range(a):
    if j == i:
        continue
