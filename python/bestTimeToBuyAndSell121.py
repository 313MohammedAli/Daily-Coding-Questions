
prices = [7,1,5,3,6,4]
best = 0
for i in range(len(prices) - 1):
    for k in range(i + 1, len(prices)):
        if prices[k] > prices[i]:
            if (prices[k] - prices[i] > best):
                best = prices[k] - prices[i]
print(best)
