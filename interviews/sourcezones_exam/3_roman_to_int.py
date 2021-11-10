roman_symbol = {
    "I": 1, 
    "V": 5, 
    "X": 10, 
    "L": 50, 
    "C": 100, 
    "D": 500, 
    "M": 1000
}

def roman_to_int(s):

    num = 0
    c = 0
    while c < len(s):
        # (前面 < 後面) => need substraction
        if c+1 < len(s) and roman_symbol[s[c+1]] > roman_symbol[s[c]]:  
            num = num + roman_symbol[s[c+1]] - roman_symbol[s[c]]
            c+=1
        # (前面 > 後面) => 直接加
        else:
            num = num + roman_symbol[s[c]]
        c+=1

    return num


if __name__ == '__main__':
    # s = "MCMXCIV"
    s = "MXLVI"
    print(roman_to_int(s))
