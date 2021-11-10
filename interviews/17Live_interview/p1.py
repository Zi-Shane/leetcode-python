# range[A, B]中, 找有 X*(X+1) 的數字有幾個

def solution(A, B):
    count = 0
    for i in range(A, B+1):
        for j in range(1, i):
            if j*(j+1) == i:
                count += 1
                
    return count

if __name__ == '__main__':
    """
    there are three numbers meet the condition between [6, 20].
    6 = 2 * 3
    12 = 3 * 4
    20 = 4 * 5
    answer = 3.
    """
    ans = solution(6, 20)
    print(ans)
