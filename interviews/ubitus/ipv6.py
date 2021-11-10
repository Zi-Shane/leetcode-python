def convert_zero(input):
    output = ""
    flag = 0
    for c in input:
        if c == ':':
            output += c
            flag = 0
        elif c != '0':
            output += c
            flag = 1
        elif c == '0' and flag == 1:
            output += c

    return output

def convert_colon(input):
    output = ""
    max_index = 0
    max_val = 0
    col_map = {}
    i = 0
    while i < len(input):
        if input[i] == ':' and input[i+1] == ':':
            count = 0
            start = i
            while input[i] == ':':
                count += 1
                i += 1
            col_map[start] = count
            if count > max_val:
                max_val = count
                max_index = start
        i += 1

    input_index = 0
    for key, value in col_map.items():
        output += input[input_index:key]
        if input_index == 0:
            input_index += key
        if key == max_index:
            output += "::"
            input_index = key
        else:
            j = value
            insert_zero = ""
            while j > 1:
                insert_zero += ":0"
                j -= 1
            insert_zero += ":"
            output += insert_zero
        input_index += value
    output += input[input_index:]

    return output

if __name__ == '__main__':
    # input = "21DA:0000:0000:0000:02AA:000F:FE08:9C5A"
    # input = "21DA:0103:0000:0000:02AA:000F:FE08:9C5A"
    # input = "21DZ:0000:0000:0000:02AA:000F:FE08:9C5A"
    input = "2001:0000:0DB8:1111:0000:0000:0000:0200"

    tmp = convert_zero(input)
    print(tmp)
    print(convert_colon(tmp))
    # 21DA::2AA:F:FE08:9C5A
    # 21DA:103::2AA:F:FE08:9C5A
    # It's not a IPv6 address!
    # 2001:0:db8:1111::200
