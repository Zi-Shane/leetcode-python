"""
Give a string of binary number, and process with following conditions.
if X is even, X = X / 2
if X is odd, X = X -1
How many steps can make X equal to 0?
"""
def solution(S):
    # write your code in Python 3.6
    count = 0
    dec = int(S, 2)
    new_str = "{0:b}".format(dec)
    l = len(new_str)-1
    while l != 0:
        if new_str[l] == 1:
            l -= 1
            count += 2
        else:
            l -= 1
            count += 1
    count += 1
    return count
    
    # while dec:
    #     if dec % 2 == 0:
    #         dec = dec // 2
    #         count += 1
    #     else:
    #         dec = dec - 1
    #         count += 1

    return count

if __name__ == '__main__':
    ans = solution('011100') # answer = 7
    # ans = solution('111') # answer = 5
    # ans = solution('1111010101111') # answer = 22
    print(ans)
