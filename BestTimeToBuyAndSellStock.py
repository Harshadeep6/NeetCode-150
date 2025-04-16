def maxProfit(prices):
  left, maxxProfit = 0, 0

  for right in range(1, len(prices)):
    if prices[right] < prices[left]:
      left = right
    else:
      maxxProfit = max(maxxProfit, prices[right] - prices[left])
  
  return maxxProfit

prices = [2,1,2,1,0,1,2]

print(maxProfit(prices))