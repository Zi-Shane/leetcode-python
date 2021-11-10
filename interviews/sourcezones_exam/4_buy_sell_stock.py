# ---
# firt tried

def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

def max_profit1(prices):
    profits = []

    # 計算出所有profits
    for i in range(len(prices)):
        if i+1 != len(prices):
            buy = prices[i]
            sell = find_max(prices[i+1:len(prices)])
            profits.append(sell - buy)  # 保留最大profit

    # profits中，找maximum
    profit = find_max(profits)
    return profit

# ---
# second tried

def max_profit2(prices):

    profit = 0
    min_price = 10000

    for i in range(len(prices)):
        # 更新最小值
        if prices[i] < min_price:
            min_price = prices[i]

        # 計算profit
        new_profit = prices[i] - min_price

        if new_profit > profit:
            profit = new_profit  # 更新profit

    return profit


if __name__ == '__main__':

    prices = [7,3,100,1,5,6,4]

    print(max_profit2(prices))

