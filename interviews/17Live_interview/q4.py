    """
Give a Binary Search function with some mistake
How many element in input array can be find by this funciton.
    
func(sequence, target)
  while sequence is not empty
    randomly choose an element from sequence as the pivot
    if pivot = target, return true
    else if pivot < target, remove pivot and all elements to its left from the sequence
    else, remove pivot and all elements to its right from the sequence
  end while
  return false

func solve(arr []int) int {
  # maximum at most right && minimum at most left => return 2
  # maximum at most right => return 1
  # minimum at most left => return 1
  -----
  # minimum at most right => return 1 (when pivot == target)
  # maximum at most left => return 1 (when pivot == target)

}

Input: nums = [-1,5,2]
Output: 1

    """
