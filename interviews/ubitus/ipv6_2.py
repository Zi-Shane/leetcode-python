input = "0abc:abc:0000:0abc:000:0100:cde:def"
output = ""

# 
flag = 0
for c in input:
    if c == ':':
        flag = 0
        output += c
    elif c != '0':
        output += c
        flag = 1
    elif c == '0' and flag == 1:
        output += c
    # c == '0' and flag == 0 pass

print(output)

# 
dic_colon = {}

i = 0
while i < len(output):
    if output[i] == ':' and output[i+1] == ':':
        start = i
        count = 0
        while output[i] == ':':
            count += 1
            i += 1
        dic_colon[start] = count
    else:
        i += 1

print(dic_colon)


# find max
max_index = 0
max_value = 0
for key, value in dic_colon.items():
    if value > max_value:
        max_index = key
        max_value = value
        
ans = ""
start = 0
for key, value in dic_colon.items():
    ans += output[start:key]
    start = key
    if key == max_index:
        ans += "::"
        start += value
    else:
        l = value
        tmp = ""
        while l > 1:
            tmp += ":0"
            l -= 1
        tmp += ":"
        ans += tmp
        start += value

ans += output[start:]
print(ans)
