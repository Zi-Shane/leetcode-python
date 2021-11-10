words = {3: "Fizz", 5: "Buzz"}

n = 15
ans = []
for i in range(1, n+1):
    ans.append(int(not(i%3)) * "Fizz" + int(not(i%5)) * "Buzz" or i)

print(ans)
