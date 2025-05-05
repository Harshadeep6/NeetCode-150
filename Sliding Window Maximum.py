def maxSlidingWindow(nums, k):
    
    maxx = float("-inf")
    maxInd = 0
    res = []
    l = 1
    for ind, val in enumerate(nums):
        if ind == k: break
        
        if val > maxx:
            maxx = val
            maxInd = ind
        
    res.append(maxx)
    for r in range(k, len(nums)):
        if l > maxInd:
            maxx = float("-inf")
            for j in range(l, r + 1):
                if nums[j] > maxx:
                    maxx = nums[j]
                    maxInd = j
            res.append(maxx)
            l += 1
            continue
            
        if nums[r] > maxx:
            maxx = nums[r]
            res.append(maxx)
        else:
            res.append(maxx)
            
        l += 1
    
    print(res)

# My output = [2, 2, 1, 0, 4]        
inds = [0, 1, 2, 3, 4, 5, 6]
nums = [1,3,-1,-3,5,3,6,7]
k = 3

maxSlidingWindow(nums, k)