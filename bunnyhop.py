
def main(): 
    arr = [1,2,3,4,2,9,2,1,2,3,2,2,3,9,10]
    bunnyhop(arr, len(arr))
    print(countways(10))
def bunnyhop(arr, n): 
    
    jumps = [0 for each in range(n)] # set the 0 for each destination
    # we start at arr[0] and it takes zero jumps to get there
    if n == 0 or arr[0] == 0: # can't move ret
        return None
    jumps[0] = 0

    for outer in range(1, n): 
        jumps[outer] = n # initially set to max
        for inner in range(0, outer): 
            # arr[inner] the size of the jump
            # inner is the current position in the array
            if outer <= inner + arr[inner] and jumps[inner] != n: 
                jumps[outer] = min(jumps[outer], jumps[inner] + 1)
                break
    print(jumps)
    return jumps

#dynamic
def countways(n): # n is num steps, we can take 1,2 or 3 steps
    if n == 0: 
        print("Can't Count Ways to Get 0")
        return
    if n == 1: 
        return 1
    result = [0] * (n+1)
    result[0] = 1 # ways to get zero
    result[1] = 1 # ways to get one 
    result[2] = 2 # ways to get two
    
    for i in range(3, n + 1): 
        result[i] = result[i - 3] + result[i - 2] + result[i - 1] # ways to get i generated with the ways to get the three previous numbers
    print(result)
    return result[n] # ways to get n
    



# find the only single number
# all of the bits will be xored out except for the single number
# ie 2's bits will eventually xor another twos bits
# relies on all elements appearing twice except one. 
# even if pairs don't follow they will flip the bits inthe same way in the end and clear all but the odd one. 

#  int singleNumber(vector<int>& nums) {
#         int x=0;
#         for(int i=0;i<nums.size();i++)
#             x = x^nums[i]; # xor
#         return x;
#     }




if __name__ == "__main__": 
    main()